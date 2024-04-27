
from django.urls import path

from src._htmx.views import (
    search_pages2,
    search_pages,
    add_menu_content,
    cms_menu_structure_save,
    update_menu_name
)


app_name = '_htmx'

urlpatterns = [
    path('search-pages/', search_pages, name='search-pages'),
    path('search-results/', search_pages, name='search-results'),
    path('add-content-to-menu/', add_menu_content, name='add-content-to-menu'),
    path('menu-structure-save/', cms_menu_structure_save, name='menu-structure-save'),
    path('menu-update-name/<int:menu_id>', update_menu_name, name='menu-update-name'),
]