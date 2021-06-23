from django.urls import path,include
from . import views

urlpatterns = [

    path('create/', views.CreateOrder.as_view()),
    path('all/', views.AllOrders.as_view()),

]
