from rest_framework import serializers
from .models import *

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta: model = SocialLink; fields = ["id", "platform", "url"]

class CompanySettingsSerializer(serializers.ModelSerializer):
    socials = serializers.SerializerMethodField()
    class Meta:
        model = CompanySettings
        fields = ["name", "logo", "description", "email", "phone", "socials"]
    def get_socials(self, obj):
        return SocialLinkSerializer(SocialLink.objects.all(), many=True).data

class ServiceSerializer(serializers.ModelSerializer):
    class Meta: model = Service; fields = "__all__"

class TrainingSerializer(serializers.ModelSerializer):
    class Meta: model = TrainingProgram; fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = ProjectCategory; fields = ["id", "name"]

class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta: model = Project; fields = "__all__"

class ContactCreateSerializer(serializers.ModelSerializer):
    website = serializers.CharField(required=False, allow_blank=True, write_only=True)  # honeypot
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message", "website"]
    def validate_message(self, v):
        if len(v.strip()) < 10:
            raise serializers.ValidationError("Le message doit contenir au moins 10 caractères.")
        return v
    def create(self, data):
        data.pop("website", None)
        return super().create(data)

class ContactAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage; fields = "__all__"
        read_only_fields = ["name", "email", "phone", "subject", "message", "created_at", "updated_at"]
