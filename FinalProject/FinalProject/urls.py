"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from FinalApp import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from FinalApp.views import CustomerView, AddressView, OrderView, OrderItemsView
# from FinalApp.ViewSets import AddressViewSet
from FinalApp.views import CustomerListCreate, AddressListCreate, OrderListCreate, OrderItemsListCreate



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url('FinalProject/add_customer', views.createCustomer, name='create_customer'),
    path('FinalProject/createAddress/<int:fk>/', views.createAddress, name='create_address'),
    path('FinalProject/createOrder/<int:fk>/', views.createOrder, name='create_order'),
    url(r'^listCustomerJSON/$', CustomerView.as_view(), name='list_customer_json'),
    url(r'^createCustomerJSON/$', CustomerView.as_view(), name='create_customer_json'),
    url(r'^listAddressJSON/$', AddressView.as_view(), name='list_address_json'),
    url(r'^createAddressJSON/$', AddressView.as_view(), name='create_address_json'),
    url(r'^listAddressREST/(?P<fk>\d+)/$', AddressListCreate.as_view(), name='list_address_REST'),
    url(r'^listOrderJSON/$', OrderView.as_view(), name='list_order_json'),
    url(r'^createOrderJSON/$', OrderView.as_view(), name='create_order_json'),
    url(r'^listOrderREST/(?P<fk>\d+)/$', OrderListCreate.as_view(), name='list_order_REST'),
    url(r'^listOrderItemsJSON/$', OrderItemsView.as_view(), name='list_orderitems_json'),
    url(r'^createOrderItemsJSON/$', OrderItemsView.as_view(), name='create_orderitems_json'),
    url(r'^listOrderItemsREST/(?P<fk>\d+)/$', OrderItemsListCreate.as_view(), name='list_orderitems_REST'),
]
