from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')

    def __str__(self):
        return self.name