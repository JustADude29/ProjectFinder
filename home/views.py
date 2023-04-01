from django.shortcuts import render


def index(request):
    return render(request, "home/home_page.html")


def login_page(request):
    return render(request, "home/Authentication_Templates/login.html")


# def login(request):
#