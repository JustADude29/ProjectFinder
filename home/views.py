from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "home/home_page.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST['InputEmail']
        password = request.POST['InputPassword']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("error logging in"))
            return redirect('login_page')
    else:
        return render(request, "home/Authentication_Templates/login.html", {})


def logout_user(request):
    logout(request)
    # messages.success(request, ("logged out!"))
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, "home/Authentication_Templates/register.html", {
        'form':form,
    })