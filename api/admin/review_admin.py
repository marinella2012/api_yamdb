from django.contrib import admin

from ..models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'author', 'score', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'text', 'author')
