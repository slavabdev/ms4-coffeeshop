from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_bag, name='the_bag'),
    path('add/<item_id>/', views.add_item_bag, name='add_item_bag'),
]