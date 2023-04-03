from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-user', views.login_user, name="login_page"),
    path('logout-user', views.logout_user , name="logout_page"),
    path('register-user', views.register_user , name="register_page"),
]