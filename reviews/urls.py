from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<slug:product_slug>/',
         views.add_review, name='add_review'),
    path('edit_review/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete/<slug:product_slug>/<int:review_id>/',
         views.delete_review, name='delete_review'),
]
