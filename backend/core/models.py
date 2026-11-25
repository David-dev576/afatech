from django.core.exceptions import ValidationError
from django.db import models


def validate_image(f):
    if f.size > 3 * 1024 * 1024:
        raise ValidationError("Image trop lourde (3 Mo maximum).")


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompanySettings(Timestamped):
    name = models.CharField(max_length=120, default="AFA TECH SOLUTIONS")
    logo = models.ImageField(upload_to="branding/", blank=True, validators=[validate_image])
    description = models.TextField(blank=True)
    email = models.EmailField(default="afatechsolution@gmail.com")
    phone = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name_plural = "company settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class SocialLink(Timestamped):
    platform = models.CharField(max_length=30, help_text="ex: facebook, linkedin, instagram, x-twitter, whatsapp, github")
    url = models.URLField()

    class Meta:
        ordering = ["platform"]


class Service(Timestamped):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=60, default="fa-solid fa-laptop-code")
    summary = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="services/", blank=True, validators=[validate_image])
    position = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self):
        return self.title


class TrainingProgram(Timestamped):
    STATUS = [("available", "Disponible"), ("planned", "Prévu")]
    title = models.CharField(max_length=160)
    track = models.CharField(max_length=40, help_text="ex: WEB 1, WEB 2")
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Séparées par des virgules")
    status = models.CharField(max_length=10, choices=STATUS, default="available")
    position = models.PositiveSmallIntegerField(default=0)
    is_published = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self):
        return self.title


class ProjectCategory(Timestamped):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = "project categories"

    def __str__(self):
        return self.name


class Project(Timestamped):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT, related_name="projects")
    summary = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, validators=[validate_image])
    github_url = models.URLField(blank=True, help_text="Lien vers le dépôt GitHub du projet (facultatif)")
    is_demo = models.BooleanField(default=True, help_text="Projet de démonstration (non livré à un client)")
    is_published = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ContactMessage(Timestamped):
    STATUS = [("new", "Nouveau"), ("read", "Lu"), ("archived", "Archivé")]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=4000)
    status = models.CharField(max_length=10, choices=STATUS, default="new", db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"