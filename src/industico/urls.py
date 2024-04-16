from django.urls import path, include
from src.industico import views


app_name = 'frontend'

urlpatterns = [
     # /author/admin/
     path('', views.index, name='index'),
     path('home-two/', views.index2, name='index2'),
     path('home-three/', views.index3, name='index3'),

     path('about-us-1/', views.about1, name='about1'),
     path('about-us-2/', views.about2, name='about2'),

     path('services-1/', views.services1, name='services1'),
     path('services-2/', views.services2, name='services2'),
     path('service/<slug:slug>/', views.service_detail, name='service-detail'),
     path('service/left/<slug:slug>/',
          views.service_detail_left, name='service-detail-left'),
     path('service/right/<slug:slug>/',
          views.service_detail_right, name='service-detail-right'),

     path('our-team/', views.our_team, name='our-team'),
     path('team-member/<slug:slug>/', views.team_member, name='team-member'),
     path('contact-us/', views.contact_us, name='contact-us'),
     path('faq/', views.faq, name='faq'),

     # Blogs
     path('blog/', views.blog_classic, name='blog'),
     path('blog-grid/', views.blog_grid, name='blog-grid'),
     path('blog-grid-4-column-full-width/', views.blog_4_column,
          name='blog-grid-4-column-full-width'),
     path('blog-grid-2/', views.blog_2_column, name='blog-grid-2'),
     path('blog-grid-2-column-left-sidebar/', views.blog_2_column_left_sidebar,
          name='blog-grid-2-column-left-sidebar'),
     path('blog-grid-2-column-right-sidebar/', views.blog_2_column_right_sidebar,
          name='blog-grid-2-column-right-sidebar'),

     # Blog single
     path('blog/<str:year>/<str:month>/<int:day>/<slug:slug>/',
          views.blog_detail, name='blog_single'),
     path('blog/left/<str:year>/<str:month>/<int:day>/<slug:slug>/',
          views.blog_detail_left_sidebar, name='blog_detail_left_sidebar'),
     path('blog/right/<str:year>/<str:month>/<int:day>/<slug:slug>/',
          views.blog_detail_right_sidebar, name='blog_detail_right_sidebar'),

     #     Projects
     path('2-columns-modern/', views.project_2_column, name='2-columns-modern'),
     path('3-columns-standard/', views.project_3_column, name='3-columns-standard'),
     path('4-columns-full-standard/', views.project_4_column, name='4-columns-full-standard'),
     path('4-columns-full-grid/', views.project_4_column_grid, name='4-columns-full-grid'),
     path('portfolio/<slug:slug>/', views.project_portfolio, name='project-portfolio'),
]
