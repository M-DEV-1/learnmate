from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem
from .forms import ToDoItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'main/base.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

@login_required
def scheduler(request):
    return render(request, 'main/scheduler.html')

@login_required
def tasks(request):
    return render(request, 'main/tasks.html')

@login_required
def assistant(request):
    return render(request, 'main/assistant.html')

@login_required
def todo_list(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            return todo_item.save()
    else:
        form = ToDoItemForm()

    items = ToDoItem.objects.filter(user=request.user)
    return render(request, 'main/tasks.html', {'items': items, 'form': form})

@login_required
def delete_todo_item(request, item_id):
    item = get_object_or_404(ToDoItem, id=item_id, user=request.user)
    item.delete()
    return redirect('tasks')