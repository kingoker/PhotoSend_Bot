from django.contrib import admin

from bot.models import TaskManager

# Register your models here.


class TaskManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_date', 'task_time', 'published')
    list_filter = ('id', 'task_date', 'task_time', 'published')

admin.site.register(TaskManager,TaskManagerAdmin)