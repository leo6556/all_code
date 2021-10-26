from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse('Страница приложениея вомен')

def categories(request, catid):

    return HttpResponse(f'<h1>Заголовок</h1><p>{catid}hghg</p>')

def archive(request, year):
    # if int(year) > 2020:
    #     raise Http404()
    if int(year) > 2020:
        return redirect('/')   # permanent=True)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound( "<h1>Шарик ты балбес</h1>")