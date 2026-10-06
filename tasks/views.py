from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Task

FILTERS = {"all", "todo", "done"}


def back_to_list(request):
    """Go back to the list, keeping the selected filter (All / To do / Done)."""
    show = request.POST.get("show", "all")
    if show not in FILTERS:
        show = "all"
    return redirect(f"{reverse('home')}?show={show}")


def welcome(request):
    """Ask for the user's name once. It is saved in the session (no password)."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()[:30]
        if name:
            request.session["name"] = name
            return redirect("home")
    return render(request, "tasks/welcome.html", {"name": request.session.get("name", "")})


def home(request):
    name = request.session.get("name")
    if not name:
        return redirect("welcome")

    show = request.GET.get("show", "all")
    if show not in FILTERS:
        show = "all"

    tasks = Task.objects.all()
    if show == "todo":
        tasks = tasks.filter(done=False)
    elif show == "done":
        tasks = tasks.filter(done=True)

    context = {
        "name": name,
        "tasks": tasks,
        "show": show,
        "left": Task.objects.filter(done=False).count(),
        "finished": Task.objects.filter(done=True).count(),
    }
    return render(request, "tasks/home.html", context)


@require_POST
def add_task(request):
    title = request.POST.get("title", "").strip()
    if title:
        Task.objects.create(title=title[:200])
    return back_to_list(request)


@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return back_to_list(request)


@require_POST
def delete_task(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return back_to_list(request)


@require_POST
def clear_done(request):
    Task.objects.filter(done=True).delete()
    return back_to_list(request)
