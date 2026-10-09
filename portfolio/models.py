from django.core.validators import MaxValueValidator
from django.db import models


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    stack = models.CharField(
        max_length=300,
        help_text="Séparer les technologies par des virgules.",
    )
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    lien_github = models.URLField(blank=True, null=True)
    lien_demo = models.URLField(blank=True, null=True)
    en_avant = models.BooleanField(default=True)
    ordre = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', '-date_creation']

    def __str__(self):
        return self.titre

    def stack_liste(self):
        return [s.strip() for s in self.stack.split(',') if s.strip()]


class Competence(models.Model):
    class Categorie(models.TextChoices):
        BACKEND = "Backend", "Backend"
        MOBILE = "Mobile", "Mobile"
        FRONTEND = "Frontend", "Frontend"
        OUTILS = "Outils", "Outils"

    nom = models.CharField(max_length=100)
    categorie = models.CharField(
        max_length=20,
        choices=Categorie.choices,
        default=Categorie.OUTILS,
    )
    niveau = models.PositiveIntegerField(
        default=80,
        validators=[MaxValueValidator(100)],
        help_text="Niveau de 0 à 100.",
    )
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.nom