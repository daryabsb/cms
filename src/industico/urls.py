from django.urls import path, include
from src.industico import views


app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('home-two/', views.index2, name='index2'),
    path('home-three/', views.index3, name='index3'),

    path('about-us-1/', views.about1, name='about1'),
    path('about-us-2/', views.about2, name='about2'),

    path('services-1/', views.services1, name='services1'),
    path('services-2/', views.services2, name='services2'),
    path('service/<slug:slug>/', views.service_detail, name='service-detail'),
    path('service/left/<slug:slug>/', views.service_detail_left, name='service-detail-left'),
    path('service/right/<slug:slug>/', views.service_detail_right, name='service-detail-right'),

    path('our-team/', views.our_team, name='our-team'),
    path('team-member/<slug:slug>/', views.team_member, name='team-member'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('faq/', views.faq, name='faq'),
]
