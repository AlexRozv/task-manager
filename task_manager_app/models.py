from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager_app.choices import TASK_PRIORITIES


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name="workers")


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=TASK_PRIORITIES, max_length=63, null=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, null=True, related_name="tasks")
    assignees = models.ManyToManyField(Worker, related_name="tasks")
