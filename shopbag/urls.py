from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_bag, name='the_bag'),
    path('add/<item_id>/', views.add_item_bag, name='add_item_bag'),
    path('update/<item_id>/', views.update_item_bag, name='update_item_bag'),
    path('delete/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]