from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    # postiton = models.ForeignKey("Postion", max_length=100, related_name="postition", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # HR_detail = models.OneToOneField("HR.EmployeeDetail", related_name="Employee_detail", on_delete=models.SET_NULL, null=True )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: list = []

    def __str__(self):
        return str(self.email)

# class Position(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     permissions = models.ManyToManyField("Permission", verbose_name=_("permissions"))

#     def __str__(self):
#         return str(self.name)

# class Permission(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(max_length=500)
#     def __str__(self):
#         return str(self.name)
    