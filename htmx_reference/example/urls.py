from __future__ import annotations

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from example import views

urlpatterns = [
    path("", views.index),
    path("favicon.ico", views.favicon),
    path("csrf-demo/", views.csrf_demo),
    path("csrf-demo/checker/", views.csrf_demo_checker),
    path("error-demo/", views.error_demo),
    path("error-demo/trigger/", views.error_demo_trigger),
    path("middleware-tester/", views.middleware_tester),
    path("middleware-tester/table/", views.middleware_tester_table),
    path("partial-rendering/", views.partial_rendering),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)