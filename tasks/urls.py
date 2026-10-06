from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("welcome/", views.welcome, name="welcome"),
    path("add/", views.add_task, name="add"),
    path("toggle/<int:pk>/", views.toggle_task, name="toggle"),
    path("delete/<int:pk>/", views.delete_task, name="delete"),
    path("clear-done/", views.clear_done, name="clear_done"),
]
