from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Buffer, User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', )
    list_filter = ('email',)
    search_fields = ('email',)
    ordering = ('email',)


class BufferAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Buffer, BufferAdmin)
