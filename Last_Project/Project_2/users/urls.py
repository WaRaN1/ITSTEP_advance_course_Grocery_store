from django.urls import path, include
from users.views import *
from Product_shop_2.views import *


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]