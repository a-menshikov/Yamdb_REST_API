from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Даёт доступ неадмину только к GET/OPTIONS/HEAD."""

    message = 'Данный запрос недоступен для вас.'

    def has_permission(self, request, view):
        """Проверка на запросы к объекту
        Для безопасных методов всегда True."""
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)


class IsAdminUser(permissions.BasePermission):
    """Доступ только для пльзователей с ролью администратора."""

    message = 'Данный запрос недоступен для вас.'

    def has_permission(self, request, view):
        return request.user.is_admin


class IsAuthorOrModerAdminPermission(permissions.BasePermission):
    """Даёт доступ неадмину/немодеру/неавтору только к GET/OPTIONS/HEAD."""

    message = 'Данный запрос недоступен для вас.'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (
                request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author
            )
        )
