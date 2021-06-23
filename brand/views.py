from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *


class Brands(generics.ListAPIView):
    serializer_class = BrandShortSerializer
    queryset = Brand.objects.all()

class GlobalBrands(generics.ListAPIView):
    serializer_class = BrandGlobalCategorySerializer
    queryset = BrandGlobalCategory.objects.all()