
from django.urls import path

from src._htmx.views import (
     search_pages2,
     search_pages,
     add_menu_content,
     cms_menu_structure_save,
     update_menu_name,
     crm_menu_structure_save,
     crm_update_menu_name,
     crm_search_pages,
     crm_search_blogs,
     crm_add_menu_content,
     crm_add_new_menu,
     crm_add_link_to_menu,
)


app_name = '_htmx'

urlpatterns = [
     path('search-pages/', search_pages, name='search-pages'),
     path('search-results/', search_pages, name='search-results'),
     path('add-content-to-menu/', add_menu_content, name='add-content-to-menu'),
     path('cms-menu-structure-save/', cms_menu_structure_save,
          name='cms-menu-structure-save'),
     path('menu-structure-save/', crm_menu_structure_save,
          name='menu-structure-save'),
     path('menu-update-name/<int:menu_id>/',
          update_menu_name, name='menu-update-name'),

     # CRM HTMX CALLS
     path('crm-menu-update-name/<int:menu_id>/',
          crm_update_menu_name, name='crm-menu-update-name'),
     path('crm-search-pages/', crm_search_pages, name='crm-search-pages'),
     path('crm-search-blogs/', crm_search_blogs, name='crm-search-blogs'),
     path('crm-add-content-to-menu/', crm_add_menu_content,
          name='crm-add-content-to-menu'),
     path('add-new-menu/', crm_add_new_menu, name='add-new-menu'),
     path('crm-add-link-to-menu/', crm_add_link_to_menu, name='crm-add-link-to-menu'),

]
