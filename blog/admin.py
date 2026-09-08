from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ('titre', 'publie', 'date_publication')
    list_editable = ('publie',)