from django.db import models
from apps.language.models import Language


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/library/')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sentence(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    translate = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.translate} - {self.text}'