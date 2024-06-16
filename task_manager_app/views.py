from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager_app.forms import WorkerCreationForm, UpdateTaskAssigneesForm
from task_manager_app.models import Task, TaskType, Position, Worker


@login_required
def index(request):
    open_tasks_count = Task.objects.filter(is_completed=False).count()
    completed_tasks_count = Task.objects.filter(is_completed=True).count()
    workers_count = Worker.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits + 1,
        "open_tasks_count": open_tasks_count,
        "completed_tasks_count": completed_tasks_count,
        "workers_count": workers_count
    }
    return render(request, "task_manager_app/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.filter(is_completed=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["completed_task_list"] = Task.objects.filter(is_completed=True)
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        task = self.get_object()
        assignees_ids = task.assignees.all().values_list("id", flat=True)
        context["assignees_form"] = UpdateTaskAssigneesForm(
            initial={"assignees": assignees_ids}
        )
        return context


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"


class TaskUpdateAssigneesView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ("assignees", )


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager_app:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_manager_app/task_type_list.html"
    context_object_name = "task_type_list"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "task_manager_app/task_type_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task_manager_app/task_type_form.html"
    fields = "__all__"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "task_manager_app/task_type_form.html"
    fields = "__all__"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "task_manager_app/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager_app:task-type-list")


@login_required
def task_toggle_completed(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(request.GET.get("next", reverse_lazy("task_manager_app:task-list")))


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager_app:position-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerDetailView, self).get_context_data(**kwargs)
        worker = self.get_object()
        context["completed_task_list"] = worker.tasks.filter(is_completed=True)
        context["open_task_list"] = worker.tasks.filter(is_completed=False)
        return context


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = ["username", "first_name", "last_name", "position"]


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager_app:worker-list")
