from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin

from Product_shop.models import *
from Product_shop.forms import *

def main(request):
    context = Product.objects.all()
    category = Category.objects.all()
    print(Category.objects.all())
    return render(template_name="Main_product.html", request=request, context={"product_list": context,
                                                                       "category": category})

def Chuice_Product(request):
    choice_priduct_context = Product.objects.all()

def login(request):
    pass


def register(request):
    pass


