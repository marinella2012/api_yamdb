from django.contrib import admin
from .models import User, Buffer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


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
