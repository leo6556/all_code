from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator

from .forms import *
from .models import *
from .utils import *

menu = [{'title' : 'О сайте', 'url_name' : 'about'},
        {'title' : 'Добавить статью', 'url_name' : 'add_page'},
        {'title' : 'Обратная связь', 'url_name' : 'contact'},
        {'title' : 'Войти', 'url_name' : 'login'}]

women = ['Ума турман', 'Лилия Броски', 'LOLOLO', 'Joli Moli', 'Trololo']

class WomenHome(DataMixin, ListView):
    paginate_by = 1
    model = Women
    template_name = 'women/index.html'
    extra_context = {'title':'Головная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# Create your views here.
# def index(request):
#     post = Women.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'post' : post,
#         'cats' : cats,
#         'menu' : menu,
#         'title' : 'Глаавная страница',
#         'cat_selected' : 0
#     }
#     return render(request, 'women/index.html', context=context)

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'

def about(request):
    return render(request, 'women/about.html', {'title' : 'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 # Women.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu':menu, 'title':'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def show_category(request, cat_id):
#     post = get_object_or_404(Women,clug=cat_id)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#     return render(request, 'women/post.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страничка не найдена</h1>')