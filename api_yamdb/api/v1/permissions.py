from rest_framework import permissions


class IsAuthorOrModerAdminPermission(permissions.BasePermission):
    message = 'Данный запрос недоступен для вас.'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user.is_staff
                or request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author
            )
        )
