from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Import UserCreationForm for signup
from django.shortcuts import render, redirect
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Redirect to home page after signup
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', {'form': form})
