from django.contrib import admin
from django.urls import path
from Product_shop.views import *

urlpatterns = [
    path("", main, name='home'),
    path("login/", login, name='login'),
    path("register/", register, name='register'),
]