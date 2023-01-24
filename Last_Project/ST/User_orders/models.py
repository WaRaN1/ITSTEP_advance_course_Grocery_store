from django.db import models
from Product_shop.models import *

class Order(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price_one = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    base64 = models.TextField()
    name_unit = models.CharField(max_length=50)
    count = models.PositiveIntegerField(blank=True, default=1)
    prace_all = models.DecimalField(max_digits=7, decimal_places=2, blank=True)

