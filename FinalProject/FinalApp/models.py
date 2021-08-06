from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator

# Create your models here.
# model to create the customer
class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    prime_customer = models.CharField(max_length=1, null=False, default='N')
    customer_since = models.DateField(null=False, default=datetime.now())

    # determines how the output will look
    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + str(self.id)

    class Meta:
        ordering = ['first_name']
# model for address
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null=False)
    zip_code = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.street + ' ' + self.city + ' ' + self.state + ' ' + self.zip_code

    class Meta:
        ordering = ['street']
# order model
class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(null=False, default=datetime.now())
    order_total = models.FloatField(null=False)
    payment_type = models.CharField(max_length=1, null=False)
    account_number = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField(null=False, default=datetime.now()+timedelta(days=365))

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=25)
    item_quantity = models.IntegerField()

    def __str__(self):
        return str(self.order.order_number) + ' ' + self.item_description + ' ' + str(self.item_quantity)
