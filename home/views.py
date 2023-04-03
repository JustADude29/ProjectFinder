from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


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