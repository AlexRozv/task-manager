from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from task_manager_app.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name in ["username", "password1", "password2"]:
            self.fields[field_name].help_text = None

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position"
        )


class UpdateTaskAssigneesForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Change assignees"
    )

    class Meta:
        model = Task
        fields = ("assignees", )


class TaskNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
