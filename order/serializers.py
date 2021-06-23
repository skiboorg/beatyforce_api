from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from djoser.conf import settings

from .models import *
from item.models import Item

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "price",
            "discount",
            "image",
            "is_active",
            "is_present",
            "is_new"
        ]

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,required=False,read_only=True)
    status = OrderStatusSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

