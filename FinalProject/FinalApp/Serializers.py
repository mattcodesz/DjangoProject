from rest_framework import serializers

from .models import Customer, Address, Order, OrderItems

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.prime_customer = validated_data.get('prime_customer', instance.preferred_customer)
        instance.customer_since = validated_data.get('customer_since', instance.customer_since)

        instance.save()
        return instance

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)

        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.item_description = validated_data.get('item_description', instance.item_description)
        instance.item_quantity = validated_data.get('item_quantity', instance.item_quantity)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.account_number = validated_data.get('account_number', instance.account_number)

        instance.save()
        return instance

class OrderItemsSerializer(serializers.ModelSerializer):
    print('test1')
    class Meta:
        print('test2')
        model = OrderItems
        fields = "__all__"

    def create(self, validated_data):
        print('test3')
        return OrderItems.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('test4')
        instance.item_description = validated_data.get('item_description', instance.item_description)
        instance.item_quantity = validated_data.get('item_quantity', instance.item_quantity)

        instance.save()
        return instance
