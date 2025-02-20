from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'link', 'name')
    list_filter = ('language',)
    search_fields = ('name', 'language__name')
