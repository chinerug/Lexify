from django.contrib import admin
from .models import Category, Word, TranslateWord

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    search_fields = ('name',)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'category')
    list_filter = ('category',)
    search_fields = ('text',)

@admin.register(TranslateWord)
class TranslateWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'language', 'text', 'audio')
    list_filter = ('language',)
    search_fields = ('text', 'word__text')