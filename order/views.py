from rest_framework.views import APIView, Response
from rest_framework import generics
from .serializers import *
from cart.models import Cart
from .models import *


class CreateOrder(APIView):

    def post(self,request):
        print(request.data)
        cart = Cart.objects.get(client=self.request.user)
        default_status = OrderStatus.objects.get(is_default=True)

        new_order = Order.objects.create(
            client=self.request.user,
            status=default_status,
            delivery=request.data.get('delivery'),
            delivery_address=request.data.get('delivery_address'),

        )

        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=new_order,
                item=cart_item.item,
                quantity=cart_item.quantity,
            )
            cart_item.delete()
        request.user.total_summ += new_order.total_price
        request.user.save()
        return Response(status=200)


class AllOrders(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


