from django.urls import path
from . import views

urlpatterns = [
    path('phrasebooks/', views.language_list, name='phrasebook_language_list'),
    path('phrasebooks/<int:language_id>/', views.category_list, name='phrasebook_category_list'),
    path('phrasebooks/<int:language_id>/categories/<int:category_id>/', views.phrase_list, name='phrasebook_phrase_list'),
    path('api/search-phrase/', views.search_phrase, name='search_phrase'),
]