from django.contrib import admin
from .models import Category, Phrase, TranslatePhrase

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    search_fields = ('name',)

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'category')
    list_filter = ('category',)
    search_fields = ('text',)

@admin.register(TranslatePhrase)
class TranslatePhraseAdmin(admin.ModelAdmin):
    list_display = ('id', 'phrase', 'language', 'text', 'audio')
    list_filter = ('language',)
    search_fields = ('text', 'phrase__text')