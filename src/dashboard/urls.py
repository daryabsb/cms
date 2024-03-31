from django.urls import path ,include, reverse_lazy
from django.contrib.auth import views as auth_views
from src.dashboard import views as dashboard_views
from src.accounts.forms import EmailValidationOnForgotPassword
from src.accounts import views as users_views

app_name='dashboard'

urlpatterns = [
    path('users/',users_views.users,name="users"),

    path('login/',users_views.login_user,name="login"),
    path('logout/',users_views.logout_user,name="logout"),

    path('',dashboard_views.index,name="index"),

    # This Route for PasswordChange
    path('password/', users_views.password_change, name='password_change'),

    # These Routes for PasswordReset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPassword,
        success_url=reverse_lazy('dashboard:password_reset_done')),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('dashboard:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]