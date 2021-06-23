from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from djoser.conf import settings

from .models import *
from item.models import Item



class ItemSimpleCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'item',
            'quantity'
        ]

class SimpleCartSerializer(serializers.ModelSerializer):
    items = ItemSimpleCartSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = Cart
        fields = [
            'id',
            'items'
        ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemFullSimpleCartSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = CartItem
        fields = '__all__'


class FullCartSerializer(serializers.ModelSerializer):
    items = ItemFullSimpleCartSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = Cart
        fields = [
            'id',
            'items',
            'total_price'
        ]