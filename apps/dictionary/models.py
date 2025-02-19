from django.db import models
from apps.language.models import Language

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/dictionary/')

    def __str__(self):
        return self.name

class Word(models.Model):
    text = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class TranslateWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=True, null=True)
    audio = models.FileField(upload_to='audio/dictionary/', blank=True, null=True)

    def __str__(self):
        return f"{self.word.text} - {self.language.name}"