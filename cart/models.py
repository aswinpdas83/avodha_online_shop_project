from datetime import datetime
from shop.models import *
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from shop.models import Products, Categ


class CartModel(models.Model):
    cart_id = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.cart_id

class CartItemModel(models.Model):
    prod = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.prod