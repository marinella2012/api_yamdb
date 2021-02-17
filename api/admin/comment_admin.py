from django.contrib import admin
from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'text', 'author', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('review', 'text', 'author')