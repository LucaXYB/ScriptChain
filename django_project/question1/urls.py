from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders_with_users, name='orders_with_users'),
    path('users/', views.users_with_orders, name='users_with_orders'),
    path('compare/', views.compare_related_methods, name='compare_related_methods'),
]