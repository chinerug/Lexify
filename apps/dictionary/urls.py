from django.urls import path
from . import views

urlpatterns = [
    path('dictionary/', views.language_list, name='dictionary_language_list'),
    path('dictionary/<int:language_id>/', views.category_list, name='dictionary_category_list'),
    path('dictionary/<int:language_id>/categories/<int:category_id>/', views.word_list, name='dictionary_word_list'),
    path('api/search-word/', views.search_word, name='search_word'),
]