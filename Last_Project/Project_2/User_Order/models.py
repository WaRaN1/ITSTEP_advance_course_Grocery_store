from django.db import models
from Product_shop_2.models import *
from users.models import *


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=100, blank=True)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True, blank=True)
    base64 = models.TextField(blank=True)
    name_unit = models.CharField(max_length=50, blank=True)
    count = models.PositiveIntegerField(blank=True, default=1)
    prace_all = models.DecimalField(max_digits=7, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name}"


