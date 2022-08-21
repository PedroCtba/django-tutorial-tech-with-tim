from django.urls import path
from . import views

urlpatterns = [
    # Path for home page
    path("home/", views.home),
    
    # Paths for todo list's
    path("<int:id>", views.index, name="index"),

    # Path for creating a todo list
    path("create/", views.create, name="create"),

    # Path view the users todo list's
    path("view/", views.view, name="view"),
]