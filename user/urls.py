from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.register,name='register'),
    path('/signup',views.handlesignup,name='signup'),
    path('/loginuser',views.loginuser,name='loginuser'),
    path('/login', views.handleLogin, name="handleLogin"),
    path('/logout', views.handleLogout, name="handleLogout"),

]