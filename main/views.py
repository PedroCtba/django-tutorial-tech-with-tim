from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import createNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = createNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = createNewList()
    return render(response, "main/create.html", {"form": form})