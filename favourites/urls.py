from django.urls import path
from . import views

urlpatterns = [
    path('<product_slug>/', views.favourites, name='favourites'),
    path('', views.favourites_list, name='favourites_list'),

]