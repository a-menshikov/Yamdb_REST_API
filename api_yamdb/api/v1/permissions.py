from rest_framework import permissions
from user.models import ADMIN


class IsAdminOrReadOnly(permissions.BasePermission):
    """Даёт доступ неадмину только к GET/OPTIONS/HEAD."""

    message = 'Данный запрос недоступен для вас.'

    def has_permissions(self, request, view):
        """Проверка на запросы к объекту
        Для безопасных методов всегда True."""
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.role == ADMIN
                    or request.user.is_staff
                    or request.user.is_superuser
                )
            )
        )
