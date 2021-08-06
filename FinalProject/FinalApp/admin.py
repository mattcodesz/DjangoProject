from django.contrib import admin

# Register your models here.
from .models import Customer, Address, Order, OrderItems

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItems)
