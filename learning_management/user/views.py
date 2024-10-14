from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
