# Plans: a minimal Django to-do list

## Run it

```bash
pip install -r requirements.txt
python manage.py makemigrations tasks
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ and type your name once. No password needed.

## How to explain it (Django's MVT pattern)

- **Model** (`tasks/models.py`): one `Task` table with `title`, `done`, `created`.
- **View** (`tasks/views.py`): functions that handle each action: show the list, add, tick/untick, delete, clear done, ask for a name.
- **Template** (`tasks/templates/tasks/`): the HTML pages. `base.html` holds the shared layout and CSS, `home.html` shows the list, `welcome.html` asks for the name.
- **URLs** (`tasks/urls.py`): maps each address (like `/add/`) to a view.
- **Session**: the name is saved in `request.session`, so the app remembers you without any login.
- **CSRF token**: every form has `{% csrf_token %}`, Django's built-in protection against forged form posts.
