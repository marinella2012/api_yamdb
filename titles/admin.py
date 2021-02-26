from django.contrib import admin

from .models import Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'description')
    list_filter = ('year', )
    search_fields = ('name', 'year', 'category')
