from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

# Create your views here.

# menu = ['о сайте', "главная страница", "добавить статью"]
menu = [{'title': 'о сайте', 'url_name':'about'},
        {'title': 'главная страница', 'url_name':'home'},
        {'title': 'добавить статью', 'url_name':'add_page'}]


def index(request):
    # return HttpResponse('Страница приложениея вомен')
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats' : cats,
        'menu': menu,
        'title': 'главная страница',
        'cat_selected': 0
    }
    # return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'главная страница'})
    return render(request, 'women/index.html', context=context)


def about(request):

    return render(request, 'women/about.html',  {'title': 'о зайте'})

def categories(request, catid):

    return HttpResponse(f'<h1>Заголовок</h1><p>{catid}hghg</p>')

def archive(request, year):
    # if int(year) > 2020:
    #     raise Http404()
    if int(year) > 2020:
        return redirect('/')   # permanent=True)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def addpage(request):
    return HttpResponse('Добавление статтьи')

def show_post(request, post_id):
    return HttpResponse(f'Отбражение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'по рубрикам',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound( "<h1>Шарик ты балбес</h1>")