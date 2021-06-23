from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from djoser.conf import settings

from .models import *
from item.models import Item



class BrandCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCountry
        fields = '__all__'

class BrandCategoryItemSerializer(serializers.ModelSerializer):

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


class BrandCategorySerializer(serializers.ModelSerializer):
    line_items = BrandCategoryItemSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = BrandCategory
        fields = '__all__'

class BrandFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandFeature
        fields = '__all__'


class BrandIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandIngredient
        fields = '__all__'


class BrandFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandFeedback
        fields = '__all__'


class BrandVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandVideo
        fields = '__all__'


class BrandPressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPress
        fields = '__all__'


class BrandShortSerializer(serializers.ModelSerializer):
    category = BrandCategorySerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'category',
            'logo'
        ]

class BrandGlobalCategorySerializer(serializers.ModelSerializer):
    brands = BrandShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = BrandGlobalCategory
        fields = '__all__'
