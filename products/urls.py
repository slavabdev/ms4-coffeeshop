from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
