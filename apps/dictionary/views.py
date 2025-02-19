from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Language, Word, TranslateWord
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def language_list(request):
    languages = Language.objects.all()
    return render(request, 'dictionary/dictionary_language_list.html', {
        'languages': languages,
    })


def word_list(request, language_id, category_id):
    language = get_object_or_404(Language, id=language_id)
    category = get_object_or_404(Category, id=category_id)
    words = Word.objects.filter(category=category)
    translations = TranslateWord.objects.filter(language=language)
    word_translations = {}
    for word in words:
        translation = translations.filter(word=word).first()
        word_translations[word] = translation
    word_translations_list = list(word_translations.items())
    paginator = Paginator(word_translations_list, 10)
    page = request.GET.get('page')

    try:
        word_translations_page = paginator.page(page)
    except PageNotAnInteger:
        word_translations_page = paginator.page(1)
    except EmptyPage:
        word_translations_page = paginator.page(paginator.num_pages)

    return render(request, 'dictionary/dictionary_word_list.html', {
        'language': language,
        'category': category,
        'word_translations_page': word_translations_page,
    })


def category_list(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    categories = Category.objects.all()
    return render(request, 'dictionary/dictionary_category_list.html', {
        'language': language,
        'categories': categories,
    })


def search_word(request):
    query = request.GET.get('q', '').strip()
    language_id = request.GET.get('language_id')

    if not query or not language_id:
        return JsonResponse({'error': 'Неверный запрос'}, status=400)
    try:
        word = Word.objects.filter(text__icontains=query).first()
        if not word:
            return JsonResponse({'error': 'Слово не найдено'}, status=404)

        translation = TranslateWord.objects.filter(word=word, language_id=language_id).first()
        response_data = {
            'word': {
                'text': word.text,
            },
            'translation': {
                'text': translation.text if translation else None,
                'audio': translation.audio.url if translation and translation.audio else None,
            }
        }
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)