from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    and (request.user.role == 'admin'
                         or request.user.is_staff))


class IsAdministratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user
                    and request.user.is_authenticated
                    and (request.user.role == 'admin'
                         or request.user.is_staff))


class IsAuthorOrModerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return bool((request.user
                         and request.user.is_authenticated
                         and request.user == obj.author)
                        or request.user.role == 'moderator'
                        or request.user.role == 'admin')
        return True
