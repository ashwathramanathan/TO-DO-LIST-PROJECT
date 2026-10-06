# Project Name: Student To-Do List

**FDS Django Practical Project**
**Name:** Ashwath Ramanathan
**Registration Number:** RA2511056030022
**Course:** B.Tech CSE Data Science - 2nd Year, 3rd Semester

## Project

This is a simple To-Do list web application made using Django. I selected the **ToDo web application** idea from the GeeksforGeeks Django Projects list and developed a minimal version for my FDS practical.

Reference: https://www.geeksforgeeks.org/python/django-projects/

Live demo: https://to-do-list-project-chi-bay.vercel.app/

## Features

- Enter your name once (no password needed)
- Personal greeting with today's date
- Add a task
- Mark a task as completed (and undo it)
- Delete a task
- Filter tasks: All, To do, Done
- Clear all completed tasks at once
- View the number of tasks left
- Change your name

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Backend programming language |
| Django | Web framework (MVT architecture) |
| SQLite | Database to store tasks |
| HTML | Page structure and Django templates |
| CSS | Styling (CSS variables, flexbox, responsive text sizing) |
| Google Fonts | Bricolage Grotesque font |
| Git and GitHub | Version control |
| Vercel | Online deployment |

## Project Structure

```
todo_project/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── vercel.json
├── api/
│   └── index.py
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/
    ├── __init__.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/tasks/
        ├── base.html
        ├── home.html
        └── welcome.html
```

## How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Create and apply migrations

```bash
python manage.py makemigrations tasks
python manage.py migrate
```

### 4. Start the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in the browser.

## How It Works

The project follows Django's MVT structure.

- **Model:** `tasks/models.py` stores the task information (`Task`) in the database.
- **View:** `tasks/views.py` handles showing the list, adding, completing, deleting and clearing tasks, and asking for the user's name.
- **Template:** HTML files display the tasks and forms. `base.html` has the shared layout and CSS, `home.html` shows the list, `welcome.html` asks for the name.
- **URL:** `tasks/urls.py` connects URLs to the required views.
- **Session:** the user's name is saved in `request.session`, so the app remembers it without a login.
- **CSRF Token:** every form uses `{% csrf_token %}` to protect against forged form submissions.
- **Database:** SQLite is used to store the data.

The main task fields are title, completion status and creation time.


## Django Concepts Used

- MVT architecture
- Models and the ORM (`create`, `filter`, `count`, `delete`)
- Migrations
- URL routing with path converters (`<int:pk>`), `include()` and named URLs
- Template inheritance (`{% extends %}` and `{% block %}`)
- Template tags (`{% for %}`, `{% if %}`, `{% url %}`, `{% now %}`)
- Sessions
- CSRF protection (`{% csrf_token %}`)
- `@require_POST` decorator
- Shortcuts: `render`, `redirect`, `get_object_or_404`
- Input validation (trimming text and limiting length)

## Deployment

The project is deployed on Vercel.

- `vercel.json` sends all requests to `api/index.py`, which runs Django through WSGI.
- `ALLOWED_HOSTS` includes `.vercel.app` so Django accepts requests on Vercel domains.
- On Vercel the SQLite file is stored in `/tmp`, which is temporary, so saved tasks can reset.

## Basic Demo

1. Start the Django server.
2. Enter your name on the welcome page.
3. Add a new task.
4. Mark the task as completed.
5. Use the All, To do and Done filters.
6. Delete a task or clear all completed tasks.

## Future Improvements

- Separate tasks for each user with login
- Edit a task
- Task priority and due dates
- Search tasks by title
