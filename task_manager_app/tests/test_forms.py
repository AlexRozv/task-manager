from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager_app.forms import (
    WorkerCreationForm,
    WorkerUsernameSearchForm,
    TaskNameSearchForm,
    TaskTypeNameSearchForm,
    PositionNameSearchForm
)
from task_manager_app.models import Worker


class WorkerCreationFormTest(TestCase):
    def test_worker_creation_form(self):
        form_date = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
        }
        form = WorkerCreationForm(data=form_date)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_date)


class WorkerSearchFormTests(TestCase):
    def test_renew_form_username_max_length(self):
        form = WorkerUsernameSearchForm()
        self.assertTrue(
            form.fields["username"].max_length == 255
        )

    def test_renew_form_username_required(self):
        form = WorkerUsernameSearchForm()
        self.assertTrue(
            form.fields["username"].required is False
        )


class TaskSearchFormTests(TestCase):
    def test_renew_form_name_max_length(self):
        form = TaskNameSearchForm()
        self.assertTrue(
            form.fields["name"].max_length == 255
        )

    def test_renew_form_name_required(self):
        form = TaskNameSearchForm()
        self.assertTrue(
            form.fields["name"].required is False
        )


class TaskTypeSearchFormTests(TestCase):
    def test_renew_form_name_max_length(self):
        form = TaskTypeNameSearchForm()
        self.assertTrue(
            form.fields["name"].max_length == 255
        )

    def test_renew_form_name_required(self):
        form = TaskTypeNameSearchForm()
        self.assertTrue(
            form.fields["name"].required is False
        )


class PositionSearchFormTests(TestCase):
    def test_renew_form_name_max_length(self):
        form = PositionNameSearchForm()
        self.assertTrue(
            form.fields["name"].max_length == 255
        )

    def test_renew_form_name_required(self):
        form = PositionNameSearchForm()
        self.assertTrue(
            form.fields["name"].required is False
        )
