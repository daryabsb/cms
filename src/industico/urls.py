from django.urls import path, include
from src.industico import views


app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('home-three/', views.index3, name='index'),
    path('about-us-1/', views.about1, name='about1'),
    path('about-us-2/', views.about2, name='about2'),

    path('services-1/', views.services1, name='services1'),
    path('services-2/', views.services2, name='services2'),

    path('our-team/', views.our_team, name='our-team'),
]
