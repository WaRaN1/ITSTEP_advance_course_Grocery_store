from django.contrib import admin
from django.urls import path
from Product_shop_2.views import *

urlpatterns = [
    path("<int:cat>/", main),
    path('<int:cat>/<int:product>/', add_product),
    path('orders/', order_all)
]