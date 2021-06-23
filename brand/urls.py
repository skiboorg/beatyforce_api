from django.urls import path,include
from . import views

urlpatterns = [

    path('brands/', views.Brands.as_view()),
    path('brands_global/', views.GlobalBrands.as_view()),


]
