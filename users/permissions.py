from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and
                (request.user.is_admin or request.user.is_staff))


class IsAdministratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user and request.user.is_authenticated and
                (request.user.is_admin or request.user.is_staff))


class IsAuthorOrModerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return (request.user and request.user.is_authenticated and
                    (request.user == obj.author
                     or request.user.is_moderator
                     or request.user.is_admin))
        return True
