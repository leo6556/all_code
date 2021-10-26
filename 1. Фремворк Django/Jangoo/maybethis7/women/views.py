from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('Страница приожения women.')

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2021:
        return redirect('/')   # redirect('/', permanent=True) - постоянныей кувшкусе (301)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p1>')











def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ну ты и балбес, такой страницы нет, лови ошибкук 404 error</h1>')