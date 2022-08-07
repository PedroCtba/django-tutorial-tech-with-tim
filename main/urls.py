from django.urls import path
from . import views

urlpatterns = [
    # Path for home page
    path("", views.home),
    path("<str:name>", views.index, name="index"),
]