from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='username',
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        verbose_name='user role',
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pk']


class Buffer(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    code = models.CharField(max_length=8)
