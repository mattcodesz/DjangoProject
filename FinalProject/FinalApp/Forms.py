from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.functional import lazy
from django.urls import resolve
from .models import Customer, Address, Order, OrderItems
class CustomerForm(forms.Form):
    #id = forms.IntegerField(widget=forms.HiddenInput)
    PRIME_STATUS = [
        ('No', 'N'),
        ('Yes', 'Y')
    ]
    current_url = ""
    firstName = forms.CharField(max_length=25, label='Enter First Name', required=True)
    lastName = forms.CharField(max_length=25, label='Enter Last Name', required=True)
    prime_customer = forms.ChoiceField(label='Prime Customer ', required=True, choices=PRIME_STATUS)

class AddressForm(forms.Form):
    STATE_CHOICES = [
        ('SC', 'South Carolina'),
        ('NC', 'North Carolina'),
        ('GA', 'Georgia'),
        ('VA', 'Virginia'),
        ('MD', 'Maryland'),
        ('PA', 'Pennsylvania'),
        ('DE', 'Delaware'),
        ('NJ', 'New Jersey'),
        ('NY', 'New York'),
        ('CT', 'Connecticut')
    ]

    street = forms.CharField(required=True, label='Enter Street name')
    city = forms.CharField(required=True, label='Enter City')
    state = forms.ChoiceField(required=True, label='Choose State', choices=STATE_CHOICES)
    zip = forms.CharField(required=True, label='Enter Zip code')

class OrderForm(forms.Form):
    Product_choices = [
        ('Java 101', 'Java 101'),
        ('Python 101', 'Python 101'),
        ('Biology 101', 'Biology 101'),
        ('English 101', 'English 101'),
        ('Cloud Computing 101', 'Cloud Computing 101')
    ]
    Payment_Method = [
        ('C', 'Credit'),
        ('B', 'Debit'),
        ('O', 'Other')
    ]
    product = forms.ChoiceField(required=True, label='Choose Product', choices=Product_choices)
    quantity = forms.IntegerField(required=True, label='Quantity')
    payment_type = forms.ChoiceField(required=True, label='Choose Payment Method', choices=Payment_Method)
    account_number = forms.CharField(required=True, label='Account Number')
