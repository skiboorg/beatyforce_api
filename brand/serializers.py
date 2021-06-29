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

class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategory
        fields = '__all__'

class BrandFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandFeature
        fields = '__all__'

class BrandItemSerializer(serializers.ModelSerializer):

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


class BrandLineSerializer(serializers.ModelSerializer):
    items = BrandItemSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = BrandItemLine
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


class BrandFullSerializer(serializers.ModelSerializer):
    country = BrandCountrySerializer(many=False, required=False, read_only=True)
    category = BrandCategorySerializer(many=True, required=False, read_only=True)
    features = BrandFeatureSerializer(many=True, required=False, read_only=True)
    ingredients = BrandIngredientSerializer(many=True, required=False, read_only=True)
    feedbacks = BrandFeedbackSerializer(many=True, required=False, read_only=True)
    videos = BrandVideoSerializer(many=True, required=False, read_only=True)
    press = BrandPressSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Brand
        fields = '__all__'

class BrandShortSerializer(serializers.ModelSerializer):
    lines = BrandLineSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Brand
        fields = [
            'id',
            'name',
            'name_slug',
            'lines',
            'logo'
        ]

class BrandGlobalCategorySerializer(serializers.ModelSerializer):
    brands = BrandShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = BrandGlobalCategory
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
