from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class User(AbstractUser):
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=9,
        choices=UserRole.choices,
        default=UserRole.USER,
        verbose_name='Роль',
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='E-mail',
    )
    confirmation_code = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Код подтверждения',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return (
                self.role == UserRole.ADMIN
                or self.is_staff
                or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR
