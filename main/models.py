from pyexpat import model
from statistics import mode
from django.db import models

# Making a class to store data | Inheritate from django.db.models
class ToDoList(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    