from django.shortcuts import get_object_or_404, render
from .models import Category, Language, Book, Sentence
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def language_list(request):
    languages = Language.objects.all()
    return render(request, 'library/library_language_list.html', {
        'languages': languages,
    })


def category_list(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    categories = Category.objects.all()
    return render(request, 'library/library_category_list.html', {
        'language': language,
        'categories': categories,
    })


def book_list(request, language_id, category_id):
    language = get_object_or_404(Language, id=language_id)
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category, language=language)
    return render(request, 'library/book_list.html', {
        'books': books,
        'language': language,
        'category': category,
    })


def sentence_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    sentences = Sentence.objects.filter(book=book)
    paginator = Paginator(sentences, 10)
    page = request.GET.get('page')
    try:
        sentences = paginator.page(page)
    except PageNotAnInteger:
        sentences = paginator.page(1)
    except EmptyPage:
        sentences = paginator.page(paginator.num_pages)

    return render(request, 'library/book_sentence_list.html', {
        'sentences': sentences,
    })