from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from order.models import Order, Checkout
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, phone, first_name, password=None):
        if not email:
            raise ValueError('Email Field Is Required')
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            phone=phone

        )
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=50)
    phone = models.PositiveIntegerField(blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = ['phone']

    def has_perm(self, perms, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return f"{self.first_name}"
