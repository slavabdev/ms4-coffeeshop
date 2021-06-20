from django.urls import path
from . import views

urlpatterns = [
    path('', views.the_bag, name='the_bag'),
]