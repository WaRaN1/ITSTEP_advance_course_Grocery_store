from urllib import request
from django.shortcuts import render
from Product_shop_2.forms import *
from Product_shop_2.models import *
from User_Order.models import *
from users.models import *
from users.forms import UserCreationForm
from users.views import Register


def main(request, cat):
    context = Product.objects.all()
    categ = Category.objects.all()

    if cat == 0:
        cat_in_time = Product.objects.all()
    else:
        cat_in_time = Product.objects.filter(category=cat)

    if request.GET:
        id_product = Product.objects.get(id=request.GET['id_product_add'])
        user = request.user
        name = id_product.name
        category = id_product.category
        price = id_product.price
        description = id_product.description
        icon = id_product.icon
        base64 = id_product.icon.base64
        name_unit = id_product.unit
        count = request.GET['count_name']
        prace_all = float(request.GET['count_name']) * float(id_product.price)
        element = Order(user=user, name=name, category=category, price=price, description=description, icon=icon,
                        base64=base64, name_unit=name_unit, count=count, prace_all=prace_all)
        element.save()

    return render(template_name="Main_product.html", request=request, context={"product_list": context,
                                                                               "category": categ,
                                                                               "cat_in_time": [cat_in_time],
                                                                               "cat": cat})

def add_product(request, cat, product):
    context = Product.objects.all()
    category = Category.objects.all()
    info = Product.objects.get(id=product)
    cat_in_time = Product.objects.filter(category=cat)
    form = CardForms(request.GET)

    return render(template_name="Add_product.html", request=request, context={"product_list": context,
                                                                               "category": category,
                                                                               "cat_in_time": [cat_in_time],
                                                                              'form': form,
                                                                              "info": info,
                                                                              'cat': cat})

def order_all(request):
    context = Order.objects.filter(user=request.user)
    category = Category.objects.all()
    all_product = len(context)
    all_price = 0.0
    for elem in context:
        all_price += float(elem.prace_all)

    return render(template_name="Order_product.html", request=request, context={"product_list": context,
                                                                                "category": category,
                                                                                "all_product": all_product,
                                                                                "all_price": all_price})
