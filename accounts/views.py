from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from accounts.forms import  UserAdminCreationForm, UserLoginForm

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView

User = get_user_model()


class HomeTemplateView(TemplateView):
	template_name = "base/home.html"
	


class MyLoginView(LoginView):
	form_class 		= UserLoginForm

class CreateUserView(FormView):

	template_name 	= 'registration/createuser.html'
	form_class 		= UserAdminCreationForm
	success_url 	= '/'

	def form_valid(self, form):

		email=form.cleaned_data['email']
		password=form.clean_password2()
		request=self.request

		user=User.objects.create_user(email,password)
		new_user = authenticate(request, email=email, password=password)
		login(request, user)
		return super(CreateUserView, self).form_valid(form)


