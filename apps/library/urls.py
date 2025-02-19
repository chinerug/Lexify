from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.language_list, name='library_language_list'),
    path('library/<int:language_id>/', views.category_list, name='library_category_list'),
    path('library/<int:language_id>/categories/<int:category_id>/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.sentence_list, name='book_sentence_list'),
]