from django.db import models


class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200, blank=True)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_envoi']

    def __str__(self):
        return f"{self.nom} - {self.sujet or 'Sans sujet'}"