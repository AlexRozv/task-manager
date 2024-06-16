from django.urls import path

from task_manager_app.views import index, TaskListView, TaskDetailView, TaskTypeListView, TaskTypeDetailView, \
    PositionListView, PositionDetailView, WorkerListView, WorkerDetailView, TaskCreateView, TaskTypeCreateView, \
    PositionCreateView, WorkerCreateView, TaskUpdateView, TaskTypeUpdateView, PositionUpdateView, WorkerUpdateView, \
    TaskDeleteView, TaskTypeDeleteView, PositionDeleteView, WorkerDeleteView, TaskUpdateAssigneesView, \
    task_toggle_completed

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/add/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/update-assignees/", TaskUpdateAssigneesView.as_view(), name="task-update-assignees"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle-completed/", task_toggle_completed, name="task-toggle-completed"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/add/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task-types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/add/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/add/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]

app_name = "task_manager_app"
