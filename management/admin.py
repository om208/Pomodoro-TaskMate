from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models.task import Task

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'oauth_provider', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'oauth_provider')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'oauth_provider')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'oauth_provider'),
        }),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'deadline', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')
