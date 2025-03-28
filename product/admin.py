from django.contrib import admin
from .models import Product, Order, OrderItem, Payment

# Register your models here.
admin.site.register([Product, Order, OrderItem, Payment])