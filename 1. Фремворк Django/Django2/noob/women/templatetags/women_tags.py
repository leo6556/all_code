from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name='cata')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_cat():
    cats = Category.objects.all()
    return {'cats' : cats}

