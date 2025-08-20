from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_coffee, name='all_coffee'),
    path('orders/', views.orders, name='orders'),
]