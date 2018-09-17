from __future__ import unicode_literals

from django.db import models

from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin,
)

from phonenumber_field.modelfields import PhoneNumberField

from .tokens import account_activation_token



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
	email 				= models.EmailField(verbose_name = "Эл.почта", max_length=255, unique=True)

	active 				= models.BooleanField(default=False) # can login
	staff				= models.BooleanField(default=False) # staff user non super
	admin				= models.BooleanField(default=False) # superuser
	is_active 			= models.BooleanField(default=False)
	timestamp			= models.DateTimeField(auto_now_add=True)
	# confirm 		= models.BooleanField(default=False)
	# confirmed_date	= models.DateTimeField(default=False)

	USERNAME_FIELD = 'email' # username
	# USERNAME_FIELD and password are required by default
	REQUIRED_FIELDS = [] #['full_name'] # python manage.py createsuperuser


	objects = UserManager()


	def __unicode__(self):
		return self.email

	# def get_full_name(self):
	# 	return self.email
	
	def get_short_name(self):
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

		
	@property
	def get_activate_url(self):
		'Возвращает ссылку на страцицу активации аккаунта'
		return 	reverse('accounts:activate',
					args = [str( urlsafe_base64_encode(force_bytes(self.pk)) )[2:-1],
						account_activation_token.make_token(self),			
					]
				)

	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_admin(self):
		return self.admin

	# @property
	# def is_active(self):
	# 	return self.active


