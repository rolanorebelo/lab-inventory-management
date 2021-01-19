from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, empid, name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not empid:
            raise ValueError("Users must have an username")
        user = self.model(
            email = self.normalize_email(email),
            empid = empid,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, empid, name, email, password):
        user =  self.create_user(
            email = self.normalize_email(email),
            empid = empid,
            name = name,
            password = password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Userr(AbstractBaseUser):
    empid = models.CharField(verbose_name="empid",max_length=10, unique=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(verbose_name="password", max_length=60, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['empid','name','password']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
