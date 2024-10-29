from django.shortcuts import render

def homepage(request):
    return render(request, 'user/index.html')


def register(request):
    return render(request, 'user/register.html')


def login(request):
    return render(request, 'user/login.html')


def teacher_dashboard(request):
    return render(request, 'user/teacher_dashboard.html')

