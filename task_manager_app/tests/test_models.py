from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager_app.models import Position, TaskType, Task


class ModelTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), position.name)

    def test_worker_str(self):
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            position=position
        )
        self.assertEqual(
            str(worker),
            f"{worker.first_name} {worker.last_name} {worker.position}"
        )

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="test")
        self.assertEqual(str(task_type), task_type.name)

    def test_task_str(self):
        task = Task.objects.create(name="test")
        self.assertEqual(str(task), task.name)

    def test_worker_with_position(self):
        position = Position.objects.create(name="test")
        username = "test"
        password = "test123"
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position
        )
        self.assertEqual(worker.username, username)
        self.assertEqual(worker.position, position)
        self.assertTrue(worker.check_password(password))

