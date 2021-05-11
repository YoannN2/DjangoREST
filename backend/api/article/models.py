from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    """
    Model Lambda d'article
    """

    titre = models.CharField("Titre", max_length=50)
    description = models.TextField(max_length=250)
    full_text = models.TextField(max_length=500)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} by {self.author.username}, posted on {self.created_at.strftime('%d/%m/%Y')} at {self.created_at.strftime('%H:%M:%S')}"
