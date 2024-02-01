from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_random_id_model import RandomIDModel


class BaseUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class BaseUser(RandomIDModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, default='example@example.com')
    password = models.CharField(
        max_length=128, default='your_default_password')

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    profile_picture = models.CharField(max_length=500)
    background_picture = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        abstract = True


class Customer(BaseUser):
    user_name = models.CharField(max_length=225)
    at_user = models.CharField(max_length=100)
    user_bio = models.CharField(max_length=500)
    groups = models.ManyToManyField(
        "auth.Group", related_name="customer_groups")
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="customer_user_permissions")

    def __str__(self):
        return f"{self.user_name}"


class Merchant(BaseUser):
    store_name = models.CharField(max_length=225)
    at_store = models.CharField(max_length=100)
    store_description = models.CharField(max_length=500)
    groups = models.ManyToManyField(
        "auth.Group", related_name="merchant_groups")
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="merchant_user_permissions")

    def __str__(self):
        return f"{self.store_name}"
