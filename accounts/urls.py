from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from accounts.views import HomeTemplateView 

from .decorators import check_recaptcha


app_name = 'accounts'


urlpatterns = [

	path('', views.HomeTemplateView.as_view(), name='home'),
	path('createuser/', check_recaptcha(views.CreateUserView.as_view()), name="createuser",),
	path('login/', auth_views.LoginView.as_view(), name="login",),
	# path(
	# 'password_reset/',
	# auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
	# name='password_reset'
	# ),
	path('logout/', auth_views.LogoutView.as_view(), name="logout",),

	path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'), 
]