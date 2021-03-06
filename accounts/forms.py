from django import forms

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model


User = get_user_model()
from .models import Profile
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email       = forms.CharField(label = 'Эл.почта',)
    password1   = forms.CharField(label = 'Пароль', widget=forms.PasswordInput)
    password2   = forms.CharField(label = 'Подтверждение пароля', widget=forms.PasswordInput)
    phone       = forms.RegexField(
        label = 'Телефон',
        regex=r'^\+?7?\d{10,10}$', 
        error_messages={'invalid': "Телефон следует заносить в формате: +71234567890"
        })


    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin', )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)