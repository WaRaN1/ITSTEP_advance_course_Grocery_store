import base64
from django.db import models


class Icon(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="Product_shop/static/icons")
    base64 = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.base64 = base64.b64encode(self.icon.read()).decode('utf-8')
        super(Icon, self).save(*args, **kwargs)



class Unit(models.Model):   #Одиниці міри та продажу
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.price}"

