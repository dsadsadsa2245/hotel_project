from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from autorization.manager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()


    def __str__(self):
        return self.email



