from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(TaskModel, TaskAdmin)
