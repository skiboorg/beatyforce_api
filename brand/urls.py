from django.urls import path,include
from . import views

urlpatterns = [

    path('brands/', views.Brands.as_view()),
    path('brand/', views.GetBrand.as_view()),
    path('brands_global/', views.GlobalBrands.as_view()),
    path('banners/', views.GetBanners.as_view()),
    path('videos/', views.GetVideos.as_view()),
    path('press/', views.GetPress.as_view()),


]
