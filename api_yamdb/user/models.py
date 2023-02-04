from django.contrib.auth.models import AbstractUser
from django.db import models


ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
ROLES = [
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER),
]


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
