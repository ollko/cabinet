from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from accounts.views import HomeTemplateView 
from django.views.generic import TemplateView

from .decorators import check_recaptcha


app_name = 'accounts'


urlpatterns = [

    path('', views.HomeTemplateView.as_view(), name='home'),
    path('createuser/',
        check_recaptcha(views.CreateUserView.as_view()),
        name="createuser",
        ),
    path(
        'linkforlogin/',
        TemplateView.as_view( template_name = 'accounts/link_for_login.html'),
        name='link_for_login' 
    ),
    path(
        'login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'),
        name="login",
        ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'
        ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'
        ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    
    
    
    path('activateconfirm/', TemplateView.as_view( template_name = 'accounts/acc_confirm.html'), name='acc_confirm' ),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
  
    path('logout/', auth_views.LogoutView.as_view(), name="logout",),

    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'), 
]