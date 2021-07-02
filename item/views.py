from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *


class GetItem(generics.RetrieveAPIView):
    serializer_class = ItemSerializer

    def get_object(self):
        return Item.objects.get(name_slug=self.request.query_params.get('slug'))