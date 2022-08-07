from django.urls import path
from . import views

urlpatterns = [
    # Path for home page
    path("", views.home),
    
    # Paths for todo list's
    path("<int:id>", views.index, name="index"),

    # Path for creating a todo list
    path("create/", views.create, name="create"),

]