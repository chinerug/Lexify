from django.db import models
from apps.language.models import Language

class Link(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.name} - {self.language.name}"