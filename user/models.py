from django.db import models
from django.contrib.auth.models import (
                                        AbstractBaseUser, 
                                        BaseUserManager, 
                                        PermissionsMixin
                                        )
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, **other_fields):
        if first_name is None or last_name is None:
            raise TypeError('Users should have a first name and a last name')
        if email is None:
            raise TypeError('Users should have an Email')
        user = self.model(
                          first_name=first_name, 
                          last_name=last_name, 
                          email=self.normalize_email(email),
                          **other_fields
                          )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(first_name, last_name, email, password, **other_fields)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.id}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
