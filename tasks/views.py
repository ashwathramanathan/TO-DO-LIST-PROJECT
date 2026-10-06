from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

# In-memory storage (tasks reset when server restarts)
tasks_storage = {}
next_id = 1

class Task:
    def __init__(self, pk, title, done=False):
        self.pk = pk
        self.title = title
        self.done = done

def back_to_list(request):
    show = request.POST.get("show", "all")
    if show not in {"all", "todo", "done"}:
        show = "all"
    return redirect(f"{reverse('home')}?show={show}")

def welcome(request):
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
    if show not in {"all", "todo", "done"}:
        show = "all"

    all_tasks = list(tasks_storage.values())
    
    if show == "todo":
        tasks = [t for t in all_tasks if not t.done]
    elif show == "done":
        tasks = [t for t in all_tasks if t.done]
    else:
        tasks = all_tasks
    
    # Sort: unfinished first, newest on top
    tasks = sorted(tasks, key=lambda x: (x.done, -x.pk))

    context = {
        "name": name,
        "tasks": tasks,
        "show": show,
        "left": len([t for t in all_tasks if not t.done]),
        "finished": len([t for t in all_tasks if t.done]),
    }
    return render(request, "tasks/home.html", context)

@require_POST
def add_task(request):
    global next_id
    title = request.POST.get("title", "").strip()
    if title:
        tasks_storage[next_id] = Task(pk=next_id, title=title[:200])
        next_id += 1
    return back_to_list(request)

@require_POST
def toggle_task(request, pk):
    if pk in tasks_storage:
        tasks_storage[pk].done = not tasks_storage[pk].done
    return back_to_list(request)

@require_POST
def delete_task(request, pk):
    if pk in tasks_storage:
        del tasks_storage[pk]
    return back_to_list(request)

@require_POST
def clear_done(request):
    global tasks_storage
    tasks_storage = {pk: t for pk, t in tasks_storage.items() if not t.done}
    return back_to_list(request)
