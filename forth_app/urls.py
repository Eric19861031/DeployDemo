from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from forth_app import views

app_name = 'forth_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]