from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models.task import Task
from .models.pomodoro_session import PomodoroSession
from .models.user_settings import Settings

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

@admin.register(PomodoroSession)
class PomodoroSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'start_time', 'end_time', 'duration')
    search_fields = ('task__title',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'alarm_tune', 'progress_status')
    search_fields = ('user__username', 'goal', 'alarm_tune', 'progress_status')
    list_filter = ('progress_status',)
