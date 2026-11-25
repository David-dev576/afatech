from django.contrib import admin
from .models import *

admin.site.site_header = "AFA TECH SOLUTIONS — Administration"
for m in (CompanySettings, SocialLink, ProjectCategory):
    admin.site.register(m)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "position", "is_published"); list_editable = ("position", "is_published")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(TrainingProgram)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "track", "status", "is_published")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_demo", "is_published"); list_filter = ("category", "is_published")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "status", "created_at"); list_filter = ("status",)
    search_fields = ("name", "email", "message")
