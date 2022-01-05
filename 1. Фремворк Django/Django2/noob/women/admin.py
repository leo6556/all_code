from django.contrib import admin
from .models import *
# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category)

