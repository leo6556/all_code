from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')

]