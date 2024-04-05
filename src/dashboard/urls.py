from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from src.dashboard import views as dashboard_views
from src.accounts.forms import EmailValidationOnForgotPassword
from src.accounts import views as users_views

app_name = 'dashboard'

urlpatterns = [
    path('users/', users_views.users, name="users"),
    path('user-details/<int:id>/', users_views.user_details, name="user-details"),
    path('add-user/', users_views.add_user, name="add-user"),
    path('edit-user/<int:id>/', users_views.edit_user, name="edit-user"),
    path('delete-user/<int:id>/', users_views.delete_user, name="delete-user"),
    path('delete-multiple-user/', users_views.delete_multiple_user,
         name="delete-multiple-user"),
    #     path('reels/', include('dashboard.cms.reels.urls', namespace='reels')),

    path('login/', users_views.login_user, name="login"),
    path('logout/', users_views.logout_user, name="logout"),
    path('groups/', users_views.groups_list, name="groups"),
    path('group-edit/<int:id>/', users_views.group_edit, name="group-edit"),
    path('group-delete/<int:id>/', users_views.group_delete, name="group-delete"),
    path('group-add/', users_views.group_add, name="group-add"),
    path('permissions/', users_views.permissions, name="permissions"),
    path('edit-permissions/<int:id>/',
         users_views.edit_permissions, name="edit-permissions"),
    path('delete-permissions/<int:id>/',
         users_views.delete_permissions, name="delete-permissions"),
    path('assign-permissions-to-user/<int:id>/',
         users_views.assign_permissions_to_user, name="assign-permissions-to-user"),
    path('signup/', users_views.signup, name="signup"),
    path('activate/<uidb64>/<token>/', users_views.activate, name='activate'),

    # CMS Links
    path('pages/', include('src.pages.urls', namespace='pages')),
    path('blogs/', include('src.blogs.urls', namespace='blog')),
    path('comments/', include('src.comment.urls', namespace='comment')),
    path('menus/', include('src.menu.urls', namespace='menu')),

    path('', dashboard_views.index, name="index"),

    # This Route for PasswordChange
    path('password/', users_views.password_change, name='password_change'),

    # These Routes for PasswordReset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPassword,
        success_url=reverse_lazy('dashboard:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('dashboard:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
