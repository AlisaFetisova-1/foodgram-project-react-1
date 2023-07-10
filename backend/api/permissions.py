from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    """Права доступа только у автора или админа."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_superuser)
