from django.urls import path,include
from . import views

urlpatterns = [
        path('simple/', views.SimpleCart.as_view()),
        path('full/', views.FullCart.as_view()),
        path('add_to_cart/', views.AddToCart.as_view()),
        path('add_quantity/', views.AddQuantity.as_view()),
        path('remove_quantity/', views.RemoveQuantity.as_view()),
        path('remove_item/', views.RemoveItem.as_view()),

]
