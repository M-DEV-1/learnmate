from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/base.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def scheduler(request):
    return render(request, 'main/scheduler.html')