from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import models
from django.contrib.auth.models import User

# Create a class fopr user registration inheritating from UserCreationForm
# Why? The user is already being stored at django admin panel
# Yes, but, we want to save the user ion the users databases as well, so its important
# to make a form for the user regsitration class=, so you can user djangos forms features
# To sabve migrations to the database!

# This class now, will be the class used at views .py file for creating userss
class RegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
