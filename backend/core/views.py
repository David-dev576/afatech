from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle
from .models import *
from .serializers import *


class PublicReadAdminWrite(permissions.BasePermission):
    """Lecture publique, écriture réservée aux administrateurs."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class PublishableViewSet(viewsets.ModelViewSet):
    """Public : éléments publiés uniquement. Administrateur : tout."""
    permission_classes = [PublicReadAdminWrite]

    def get_queryset(self):
        qs = super().get_queryset()
        u = self.request.user
        return qs if (u and u.is_staff) else qs.filter(is_published=True)


class ServiceViewSet(PublishableViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TrainingViewSet(PublishableViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingSerializer


class ProjectViewSet(PublishableViewSet):
    queryset = Project.objects.select_related("category")
    serializer_class = ProjectSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [PublicReadAdminWrite]
    queryset = ProjectCategory.objects.all()
    serializer_class = CategorySerializer


class SocialLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [PublicReadAdminWrite]
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    throttle_scope = "contact"

    def get_throttles(self):
        # Limite anti-spam uniquement sur l'envoi d'un message
        return [ScopedRateThrottle()] if self.action == "create" else []

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        return ContactCreateSerializer if self.action == "create" else ContactAdminSerializer

    def create(self, request, *args, **kwargs):
        if request.data.get("hp_check"):  # piège anti-spam déclenché
            return Response({"detail": "Message reçu."}, status=status.HTTP_201_CREATED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Message reçu."}, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([PublicReadAdminWrite])
def company_settings(request):
    obj, _ = CompanySettings.objects.get_or_create(pk=1)
    if request.method == "GET":
        return Response(CompanySettingsSerializer(obj, context={"request": request}).data)
    serializer = CompanySettingsSerializer(obj, data=request.data, partial=True, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class LoginThrottle(AnonRateThrottle):
    """Limite les tentatives de connexion (scope « login », 10 par heure)."""
    scope = "login"


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@throttle_classes([LoginThrottle])
def login(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if not user or not user.is_staff:
        return Response({"detail": "Identifiants invalides."}, status=400)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "username": user.username})


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response(status=204)


def _profile_data(u):
    return {"username": u.username, "first_name": u.first_name, "email": u.email}


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def me(request):
    return Response(_profile_data(request.user))


@api_view(["PATCH"])
@permission_classes([permissions.IsAdminUser])
def update_profile(request):
    u = request.user
    email = str(request.data.get("email", u.email)).strip()
    if email:
        try:
            validate_email(email)
        except ValidationError:
            return Response({"email": ["Adresse e-mail invalide."]}, status=400)
    u.first_name = str(request.data.get("first_name", u.first_name))[:150]
    u.email = email
    u.save(update_fields=["first_name", "email"])
    return Response(_profile_data(u))


@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def change_password(request):
    u = request.user
    if not u.check_password(request.data.get("old_password", "")):
        return Response({"detail": "Ancien mot de passe incorrect."}, status=400)
    try:
        validate_password(request.data.get("new_password", ""), u)
    except ValidationError as e:
        return Response({"detail": " ".join(e.messages)}, status=400)
    u.set_password(request.data["new_password"])
    u.save()
    Token.objects.filter(user=u).delete()
    return Response({"detail": "Mot de passe modifié. Reconnectez-vous."})


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def stats(request):
    return Response({
        "messages_total": ContactMessage.objects.count(),
        "messages_new": ContactMessage.objects.filter(status="new").count(),
        "services": Service.objects.count(),
        "trainings": TrainingProgram.objects.count(),
        "projects": Project.objects.count(),
        "projects_published": Project.objects.filter(is_published=True).count(),
    })