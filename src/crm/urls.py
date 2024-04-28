from django.urls import path, include
from src.crm.views import crm_index


app_name = 'crm'

urlpatterns = [
    path('', crm_index, name="crm-index"),
    path('pages/', include('src.pages.urls', namespace='crm-pages')),
    path('blogs/', include('src.blogs.urls', namespace='crm-blogs')),
]