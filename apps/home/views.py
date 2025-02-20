from django.shortcuts import render
from apps.home.models import Link
from apps.language.models import Language


def home_page(request):
    languages = Language.objects.all()
    links = Link.objects.all()
    return render(request, 'home/home_page.html', {
        'languages': languages,
        'links': links,
    })