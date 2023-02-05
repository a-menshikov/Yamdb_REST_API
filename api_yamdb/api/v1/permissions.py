from rest_framework import permissions
from user.models import ADMIN, MODERATOR


class IsAdminOrReadOnly(permissions.BasePermission):
    """Даёт доступ неадмину только к GET/OPTIONS/HEAD."""

    message = 'Данный запрос недоступен для вас.'

    def has_permission(self, request, view):
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


class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and (request.user.role == ADMIN
                                      or request.user.is_superuser))


class IsAuthorOrModerAdminPermission(permissions.BasePermission):
    message = 'Данный запрос недоступен для вас.'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user.is_staff
                or request.user.role == ADMIN
                or request.user.role == MODERATOR
                or request.user == obj.author
            )
        )
