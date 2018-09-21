from django.shortcuts import render


from django.views.generic import DetailView
from django.http import Http404

from django.contrib.auth import get_user_model
User = get_user_model()


class UserCabinetDetailView(DetailView):
	template_name = 'shop/user_cabinet.html'
	model = User

	def get(self, request, *args, **kwargs):
		if not request.user == self.get_object():
			print (not request.user == self.get_object())
			raise Http404('У вас нет прав для просмотра этой страницы')

		return super(UserCabinetDetailView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(UserCabinetDetailView, self).get_context_data(**kwargs)
	
		user = self.request.user

		context['user'] = user
		return context
