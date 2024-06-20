from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager_app.models import Task

TASK_LIST_URL = reverse("task_manager_app:task-list")
TASK_DETAIL_URL = reverse("task_manager_app:task-detail", kwargs={"pk": 1})


class PublicTaskTest(TestCase):
    def test_list_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_detail_login_required(self):
        Task.objects.create(name="test")
        res = self.client.get(TASK_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        Task.objects.create(name="open task")
        Task.objects.create(name="completed task", is_completed=True)
        res = self.client.get(TASK_LIST_URL)
        self.assertEqual(res.status_code, 200)
        open_tasks = Task.objects.filter(is_completed=False)
        completed_tasks = Task.objects.filter(is_completed=True)
        self.assertEqual(
            list(res.context["task_list"]),
            list(open_tasks)
        )
        self.assertEqual(
            list(res.context["completed_task_list"]),
            list(completed_tasks)
        )
        self.assertTemplateUsed("task_manager_app/task_list.html")

    def test_retrieve_task(self):
        task = Task.objects.create(name="test")
        res = self.client.get(TASK_DETAIL_URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context["task"], task)
        self.assertTemplateUsed("task_manager_app/task_detail.html")
