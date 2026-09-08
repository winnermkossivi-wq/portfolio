from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    resume = models.CharField(max_length=300, blank=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    publie = models.BooleanField(default=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titre) or 'article'
            slug = base
            num = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)