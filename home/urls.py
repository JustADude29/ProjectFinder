from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-user', views.login_user, name="login_page"),
]