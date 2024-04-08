from django.urls import path ,include
from src.industico import views



app_name='frontend'

urlpatterns = [
    path('', views.index, name='index'),
]