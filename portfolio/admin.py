from django.contrib import admin

from .models import Competence, Projet


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'en_avant', 'ordre', 'date_creation')
    list_editable = ('en_avant', 'ordre')


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'niveau', 'ordre')
    list_editable = ('categorie', 'niveau', 'ordre')