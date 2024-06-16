from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from task_manager_app.choices import TASK_PRIORITIES


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("task_manager_app:position-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, related_name="workers")

    def get_absolute_url(self):
        return reverse("task_manager_app:worker-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.position}"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("task_manager_app:task-type-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=TASK_PRIORITIES, max_length=63, null=True, blank=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    assignees = models.ManyToManyField(Worker, blank=True, related_name="tasks")

    def get_absolute_url(self):
        return reverse("task_manager_app:task-detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.name
