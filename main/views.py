from django.shortcuts import render
from .models import ToDoList

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "main/list.html", {"name": ls.name})

def home(response):
    return render(response, "main/home.html", {})