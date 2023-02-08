from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('cars/<int:id>', views.car_detail, name='car_detail'),
]