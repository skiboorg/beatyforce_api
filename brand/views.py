from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *


class GetBrand(generics.RetrieveAPIView):
    serializer_class = BrandFullSerializer

    def get_object(self):
        return Brand.objects.get(name_slug=self.request.query_params.get('slug'))

class Brands(generics.ListAPIView):
    serializer_class = BrandShortSerializer
    queryset = Brand.objects.all()

class GlobalBrands(generics.ListAPIView):
    serializer_class = BrandGlobalCategorySerializer
    queryset = BrandGlobalCategory.objects.all()


class GetBanners(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.filter(is_active=True)


class GetVideos(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active=True)