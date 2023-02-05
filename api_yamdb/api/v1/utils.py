from django.utils.crypto import get_random_string


def get_confirmation_code():
    """Генерирует confirmation_code."""

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*'
    return get_random_string(20, chars)
