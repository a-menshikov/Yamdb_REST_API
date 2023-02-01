from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ('ADM', 'admin'),
        ('MDR', 'moderator'),
        ('USR', 'user'),
    ]
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=3,
        choices=ROLES,
        default='USR',
    )
