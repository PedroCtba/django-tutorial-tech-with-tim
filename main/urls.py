from django.urls import path
from . import views

urlpatterns = [
    # Path for home page
    path("", views.home),
    path("<int:id>", views.index, name="index"),
]