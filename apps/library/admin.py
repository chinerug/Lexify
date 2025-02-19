from django.contrib import admin
from .models import Category, Book, Sentence


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category', 'language')
    list_filter = ('category',)
    search_fields = ('name', 'author')


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'translate', 'text')
    list_filter = ('book',)
    search_fields = ('book__name',)