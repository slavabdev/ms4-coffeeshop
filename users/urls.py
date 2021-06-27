from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('all_order_history/', views.all_order_history, name='all_order_history'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
