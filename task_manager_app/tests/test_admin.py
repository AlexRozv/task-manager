from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager_app.models import Position


class AdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="test123"
        )
        self.client.force_login(self.admin_user)
        self.position = Position.objects.create(name="test_position")
        self.worker = get_user_model().objects.create_user(
            username="worker", password="test123", position=self.position
        )

    def test_worker_position_listed(self):
        url = reverse("admin:task_manager_app_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.position)

    def test_worker_detail_position_listed(self):
        url = reverse(
            "admin:task_manager_app_worker_change", args=[self.worker.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.position)
