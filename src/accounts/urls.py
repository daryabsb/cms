from django.urls import path
from src.accounts.views import (
    crm_users,
    crm_groups_list,
    crm_permissions_list,
)


app_name = 'accounts'

urlpatterns = [
    path('users/', crm_users, name='users-list'),
    path('groups/', crm_groups_list, name='groups-list'),
    path('permissions/', crm_permissions_list, name='permissions-list'),
]