from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import createNewList

# Define todo list return
def index(response, id):
    # Take the todo list with this id
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        # If the user is sendinng
        if response.method == "POST":
        
            # If the user hits "save"
            if response.POST.get("save"):
                for item in ls.item_set.all():

                    # Pass troghout all the itens of this list and marke them as complete if they were clicked        
                    if response.POST.get("c" + str(item.id)) == "cliked":
                        item.complete = True
                    # Else let them incomplete
                    else:
                        item.complete = False
                    
                    # Save new status
                    item.save()

            # If the user click"s on new Item
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                
                # Check the lenght of item and add it
                if len(txt) > 1:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")

        # Return this page
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = createNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
        
    else:
        form = createNewList()
    return render(response, "main/create.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})