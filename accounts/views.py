from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView

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

from letters.models import Letter
from accounts.forms import  UserAdminCreationForm, UserLoginForm, ProfileForm
from .models import Profile


class HomeTemplateView(TemplateView):
    template_name = "base/home.html"
    


class MyLoginView(LoginView):
    form_class      = UserLoginForm

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
            mail_subject = 'Activate your upgram.ru account. Активация аккаунта на upgram.ru.'
            
            try:
                letter = Letter.objects.get(featured = True)
            except Letter.DoesNotExist:
                letter = None
            if letter:
                text_content, html_content = letter.text_content, letter.html_content
            else:
                text_content, html_content = (None, None)
                
            
            html_massage = '{} <p>Для подтверждения регистрации перейдите по сылке: http://{}{}</p>'.format(
                                                                        letter.html_content,
                                                                        current_site,        
                                                                        user.get_activate_url
            )

            text_message = render_to_string('registration/acc_active_email.html', {
                'user'          : user,
                'domain'        : current_site.domain,
                'uid'           : str( urlsafe_base64_encode(force_bytes(user.pk)) )[2:-1],
                'token'         : account_activation_token.make_token(user),
                "text_content"  : letter.text_content,
            })
  
            to_email = form.cleaned_data.get('email')

            # email = EmailMessage(
            #             mail_subject, text_message, to=[to_email]
            # )

            email = EmailMultiAlternatives(
                        mail_subject, text_message, to=[to_email]
            )

            email.attach_alternative(html_massage, "text/html")
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
        # return redirect('home')
        return redirect('accounts:link_for_login')
    else:
        return HttpResponse('Activation link is invalid! Активационная ссылка не действительна!')