from django.shortcuts import render

from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
from django.views import View

from .models import Customer, Address, Order, OrderItems
from .Forms import CustomerForm, AddressForm, OrderForm

from django.views.generic import ListView, UpdateView, CreateView
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializers import AddressSerializer, CustomerSerializer, OrderSerializer, OrderItemsSerializer
from django.urls import reverse, resolve

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    addresses = Address.objects.all()
    orders = Order.objects.all()
    items = OrderItems.objects.all()

    paginator = Paginator(customers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    customers = paginator.get_page(page_number)

    return render(request, 'home.html',
                  {'page_obj': page_obj, 'customers': customers, 'addresses': addresses,
                   'orders': orders, 'items': items})

def validateCustomer(form, customer):
    print("Further Validating Customer")
    print(customer)
    #form.add_error(None, "Customer first Name and Last Name combination is not unique")
    return True

def createCustomer(request):
    submitted = False
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            customer = Customer(first_name=cd['firstName'], last_name=cd['lastName'],
                                prime_customer=cd['prime_customer'])
            if validateCustomer(form, customer):
                customer.save()
            else:
                return render(request, 'create_customer.html', {'form': form})
        else:
            print(form.errors)
            return render(request, 'create_customer.html', {'form': form})
        return HttpResponseRedirect(reverse('index'))
    else:
        if 'submitted' in request.GET:
            submitted = True
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form, 'submitted': submitted})

def createAddress(request, fk):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(id=fk)
            cd = form.cleaned_data
            address = Address(street=cd['street'], city=cd['city'], state=cd['state'],
                              zip_code=cd['zip'])
            address.customer = customer
            address.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create_address.html', {'form': form})
    else:
        form = AddressForm()
        return render(request, 'create_address.html', {'form': form})

def createOrder(request, fk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(id=fk)
            cd = form.cleaned_data

            quan = cd['quantity']
            order_total = 50 * quan

            order = Order(payment_type=cd['payment_type'], account_number=cd['account_number'],
                          order_total=order_total)
            order.customer = customer
            order.save()
            filler = order.order_number
            items = OrderItems(item_description=cd['product'], item_quantity=cd['quantity'], order_id=order.order_number)
            items.save()
            print(order.order_number)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create_order.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'create_order.html', {'form': form})

# API View Section

class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        customer_data = request.data
        serializer = CustomerSerializer(data=customer_data)
        if serializer.is_valid(raise_exception=True):
            customer_saved = serializer.save()
        return Response({"success": "Customer '{}' created successfully".format(customer_saved.id)})

    def put(self, request):
        customer_data = request.data
        customer = get_object_or_404(Customer.objects.all(), pk=customer_data.get('id'))

        serializer = CustomerSerializer(instance=customer, data=customer_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            customer_saved = serializer.save()
        return Response({"success": "Customer '{}' updated successfully".format(customer_saved.id)})

class AddressView(APIView):
    def get(self, request):
        address = Address.objects.all()
        # more than one contacts are being serialized
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    def post(self, request):
        address_data = request.data

        # Create contact from the above data
        serializer = AddressSerializer(data=address_data)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"success": "Address '{}' created successfully".format(address_saved.id)})

    def put(self, request):
        address_data = request.data
        address = get_object_or_404(Address.objects.all(), pk=address_data.get('id'))

        serializer = AddressSerializer(instance=address, data=address_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"success": "Address '{}' updated successfully".format(address_saved.id)})

class OrderView(APIView):
    def get(self, request):
        order = Order.objects.all()
        # more than one contacts are being serialized
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        order_data = request.data

        # Create contact from the above data
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' created successfully".format(order_saved.id)})

    def put(self, request):
        order_data = request.data
        order = get_object_or_404(Order.objects.all(), pk=order_data.get('id'))

        serializer = OrderSerializer(instance=order, data=order_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' updated successfully".format(order_saved.id)})

class OrderItemsView(APIView):
    def get(self, request):
        orderitems = OrderItems.objects.all()
        # more than one contacts are being serialized
        serializer = OrderItemsSerializer(orderitems, many=True)
        return Response(serializer.data)

    def post(self, request):
        orderitems_data = request.data

        # Create contact from the above data
        serializer = OrderItemsSerializer(data=orderitems_data)
        if serializer.is_valid(raise_exception=True):
            orderitems_saved = serializer.save()
        return Response({"success": "OrderItems '{}' created successfully".format(orderitems_saved.id)})

    def put(self, request):
        orderitems_data = request.data
        orderitems = get_object_or_404(OrderItems.objects.all(), pk=orderitems_data.get('id'))

        serializer = OrderItemsSerializer(instance=orderitems, data=orderitems_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            orderitems_saved = serializer.save()
        return Response({"success": "OrderItems '{}' updated successfully".format(orderitems_saved.id)})

# ListCreateAPIView Section
class CustomerListCreate(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            customer = serializer.create(serializer.validated_data)
            return Response(CustomerSerializer(customer).data)

class AddressListCreate(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def list(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        address = Address.objects.filter(customer=fk)
        addressData = AddressSerializer(address, many=True)
        return Response(addressData.data)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.create(serializer.validated_data)
            return Response(AddressSerializer(address).data)

class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        order = Order.objects.filter(customer=fk)
        orderData = OrderSerializer(order, many=True)
        return Response(orderData.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.create(serializer.validated_data)
            return Response(OrderSerializer(order).data)

class OrderItemsListCreate(generics.ListCreateAPIView):
    serializer_class = OrderItemsSerializer
    queryset = OrderItems.objects.all()

    def list(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        orderitems = OrderItems.objects.filter(order=fk)
        orderitemsData = OrderItemsSerializer(orderitems, many=True)
        return Response(orderitemsData.data)

    def create(self, request, *args, **kwargs):
        fk = kwargs["fk"]
        serializer = OrderItemsSerializer(data=request.data)
        if serializer.is_valid():
            orderitems = serializer.create(serializer.validated_data)
            order = Order.objects.get(order_number=fk)
            print(order.order_total)
            print(orderitems.item_quantity)
            order.order_total += orderitems.item_quantity * 50
            order.save()
            return Response(OrderItemsSerializer(orderitems).data)