from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [

    path('<int:pk>', views.UserCabinetDetailView.as_view(), name='user-sabinet'),

]