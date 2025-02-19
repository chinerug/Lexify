from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Language, Phrase, TranslatePhrase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def language_list(request):
    languages = Language.objects.all()
    return render(request, 'phrasebook/phrasebook_language_list.html', {'languages': languages})


def phrase_list(request, language_id, category_id):
    language = get_object_or_404(Language, id=language_id)
    category = get_object_or_404(Category, id=category_id)
    phrases = Phrase.objects.filter(category=category)
    translations = TranslatePhrase.objects.filter(language=language)

    phrase_translations = {}
    for phrase in phrases:
        translation = translations.filter(phrase=phrase).first()
        phrase_translations[phrase] = translation

    phrase_translations_list = list(phrase_translations.items())

    paginator = Paginator(phrase_translations_list, 10)
    page = request.GET.get('page')

    try:
        phrase_translations_page = paginator.page(page)
    except PageNotAnInteger:
        phrase_translations_page = paginator.page(1)
    except EmptyPage:
        phrase_translations_page = paginator.page(paginator.num_pages)

    return render(request, 'phrasebook/phrasebook_phrase_list.html', {
        'language': language,
        'category': category,
        'phrase_translations_page': phrase_translations_page,
    })


def category_list(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    categories = Category.objects.all()
    return render(request, 'phrasebook/phrasebook_category_list.html', {
        'language': language,
        'categories': categories,
    })


def search_phrase(request):
    query = request.GET.get('q', '').strip()
    language_id = request.GET.get('language_id')

    if not query or not language_id:
        return JsonResponse({'error': 'Неверный запрос'}, status=400)

    try:
        phrase = Phrase.objects.filter(text__icontains=query).first()
        if not phrase:
            return JsonResponse({'error': 'Фраза не найдена'}, status=404)

        translation = TranslatePhrase.objects.filter(phrase=phrase, language_id=language_id).first()

        response_data = {
            'phrase': {
                'text': phrase.text,
            },
            'translation': {
                'text': translation.text if translation else None,
                'audio': translation.audio.url if translation and translation.audio else None,
            }
        }

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)