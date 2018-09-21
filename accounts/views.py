from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from django.contrib.auth.views import LoginView

from django.contrib.auth import get_user_model, authenticate, login
User = get_user_model()


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse


from letters.models import Letter
from accounts.forms import  UserAdminCreationForm, UserLoginForm, ProfileForm
from .models import Profile


class StartTemplateView(TemplateView):
    template_name = "base/start.html"
    


class CabinetLoginView(LoginView):
    template_name   = 'accounts/login.html'

    def form_valid(self, form):
        self.form = form
        return super(CabinetLoginView, self).form_valid( form )

    def get_success_url(self):
        user = self.form.get_user()
        self.success_url = reverse('shop:user-sabinet', args=[user.id])
        print(self.success_url)
        print(super(CabinetLoginView, self).get_success_url())
        print(self.request.GET)
        return self.success_url
        # return super(CabinetLoginView, self).get_success_url()

class CreateUserView(FormView):

    template_name   = 'accounts/createuser.html'
    form_class      = UserAdminCreationForm
    # profile_form_class     = ProfileForm
    success_url     = '/'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            email = form.cleaned_data['email']
            password = form.clean_password2()
            request = self.request

            user = User.objects.create_user(email, password, is_active = False)

            phone = form.cleaned_data['phone']
            p = Profile(user = user, phone =phone)
            p.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your upgram.ru account. Активация аккаунта на upgram.ru'
            
            try:
                letter = Letter.objects.get(featured = True)
            except Letter.DoesNotExist:
                letter = None
            if letter:
                text_content, html_content = letter.text_content, letter.html_content
            else:
                text_content, html_content = (None, None)
                
            activation_link = 'http://{}{}'.format( current_site, user.get_activate_url )
            print('activation-link')
            html_content = letter.html_content.split('[activation-link]')
            text_content = letter.text_content.split('[activation-link]')
                                                                              
            html_message = html_content[0] + activation_link + html_content[1]
            text_message = text_content[0] + activation_link + text_content[1]
  
            to_email = form.cleaned_data.get('email')


            email = EmailMultiAlternatives(
                        mail_subject, text_message, to=[to_email]
            )

            email.attach_alternative(html_message, "text/html")
            email.send()
            
            # return super(CreateUserView, self).form_valid(form)
            # return HttpResponse('Please confirm your email address to complete the registration.\n На вашу почту отправлено письмо. Для подтверждения регистрации пройдите по ссылке в письме  ')
            return redirect ('accounts:acc_confirm')
        return render(self.request, 'accounts/createuser.html', self.get_context_data())



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('start')
        return redirect('accounts:link_for_login')
    else:
        return HttpResponse('Activation link is invalid! Активационная ссылка не действительна!')