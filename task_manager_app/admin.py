from django.contrib import admin

from task_manager_app.models import Worker, Position, Task, TaskType


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "position")
    ordering = ("username",)
    list_filter = ("position",)
    search_fields = ("username",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    ordering = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "task_type",
    )
    ordering = ("name", "deadline", )
    list_filter = ("task_type", "priority", "is_completed")
    search_fields = ("name", "description", )
