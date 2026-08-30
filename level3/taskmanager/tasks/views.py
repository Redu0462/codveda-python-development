from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/home.html', {'tasks': tasks})