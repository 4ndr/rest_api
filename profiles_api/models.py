from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
	"""Helps Django work with our custom user model"""
	
	def create_user(self, email, name, password=None):
		"""Creates a new user profile object"""

		if not email:
			raise ValueError('Users most have a email address.')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Create and saves a new superuser with given details."""

		user = self.create_user(email, name, password)

		user.is_supperuser = True
		user.is_staff = True

		user.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Represent a user profile inside our system."""
	
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)


	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUERID_FIELD = ['name']

	def get_full_name(self):
		""" USed to get a users full name. """

		return self.name

	def get_short_name(self):
		"""Used to get a users short name"""

		return self.name

	def __str__(seld):
		"""Django uses this when it mades to convert the object to a string"""

		return self.email

		
