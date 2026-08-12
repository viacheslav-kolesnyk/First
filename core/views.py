from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from core.models import Task, Tag
from core.forms import TaskForm


# --- TASK VIEWS ---
class TaskListView(generic.ListView):
    model = Task
    template_name = "core/index.html"
    context_object_name = "tasks"


# Keep all your other existing views (TaskListView, TaskDeleteView, Tag views, etc.) exactly the same!
class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm  # Replaces fields = [...]
    template_name = "core/task_form.html"
    success_url = reverse_lazy('core:index')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm  # Replaces fields = [...]
    template_name = "core/task_form.html"
    success_url = reverse_lazy('core:index')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "core/task_confirm_delete.html"
    success_url = reverse_lazy("core:index")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("core:index")


# --- TAG VIEWS ---
class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "core/tag_form.html"
    success_url = reverse_lazy("core:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ['name']
    template_name = "core/tag_form.html"
    success_url = reverse_lazy("core:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "core/tag_confirm_delete.html"
    success_url = reverse_lazy("core:tag-list")
