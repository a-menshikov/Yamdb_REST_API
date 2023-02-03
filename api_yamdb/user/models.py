from django.contrib.auth.models import AbstractUser
from django.db import models

from user.constants import ROLES


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=9,
        choices=ROLES,
        default='user',
    )
