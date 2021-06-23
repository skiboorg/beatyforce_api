from rest_framework.views import APIView, Response
from rest_framework import generics
from .serializers import *
from .models import *

def getCart(request):
    return Cart.objects.get(client=request.user)

def calculateCarttotalPrice(cart):
    items = cart.items.all()
    price = 0
    for i in items:
        price += i.price
    cart.total_price = price
    cart.save()
    return

class SimpleCart(generics.RetrieveAPIView):
    serializer_class = SimpleCartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(client=self.request.user)
        if created:
            print('cart created')
        return cart

class FullCart(generics.RetrieveAPIView):
    serializer_class = FullCartSerializer

    def get_object(self):
        return Cart.objects.get(client=self.request.user)


class AddToCart(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        cart = getCart(self.request)

        CartItem.objects.create(cart=cart,
                                item_id=id,
                                quantity=1)
        calculateCarttotalPrice(cart)
        return Response(status=200)

class AddQuantity(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        cart_item = CartItem.objects.get(item_id=id)
        cart_item.quantity += 1
        cart_item.save()
        calculateCarttotalPrice(cart_item.cart)
        return Response(status=200)

class RemoveQuantity(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        cart_item = CartItem.objects.get(item_id=id)
        cart = cart_item.cart
        if cart_item.quantity - 1 == 0:
            cart_item.delete()
            calculateCarttotalPrice(cart)
        else:
            cart_item.quantity -= 1
            cart_item.save()
        calculateCarttotalPrice(cart)
        return Response(status=200)

class RemoveItem(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        cart_item = CartItem.objects.get(id=id)
        cart = cart_item.cart
        cart_item.delete()
        calculateCarttotalPrice(cart)
        return Response(status=200)

