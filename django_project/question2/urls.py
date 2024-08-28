from django.urls import path
from . import views

urlpatterns = [
    path('q-object-queries/', views.q_object_queries, name='q_object_queries'),
]
