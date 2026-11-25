from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("services", views.ServiceViewSet)
router.register("training", views.TrainingViewSet)
router.register("projects", views.ProjectViewSet)
router.register("categories", views.CategoryViewSet)
router.register("socials", views.SocialLinkViewSet)
router.register("messages", views.ContactViewSet)

urlpatterns = [
    path("settings/", views.company_settings),
    path("auth/login/", views.login),
    path("auth/logout/", views.logout),
    path("auth/me/", views.me),
    path("auth/profile/", views.update_profile),
    path("auth/password/", views.change_password),
    path("stats/", views.stats),
    path("", include(router.urls)),
]