from django.contrib import admin

from ..models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'title')
    list_filter = ('name', )
    search_fields = ('name', 'slug', 'title')
