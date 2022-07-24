from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username  = form.cleaned_data.get("username")
            password  = form.cleaned_data.get("password") 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return # redirect to Home page
    else:
        form = LoginForm()
    context = {'form': form}
    return # render the login page


def logout_user(request):
    logout(request)
    return # redirect to the login page


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        password = request.POST['password1']
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return # redirect to the login page
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return # render the registration page
