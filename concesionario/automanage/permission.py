from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def __init__(self, roles_required):
        self.roles_required = roles_required

    def has_permission(self, request, view):
        # print(request.user)
        # print(request.user.rol.nombre)
        # print(self.roles_required)
        if request.user and request.user.is_authenticated:
            if request.user.is_admin or request.user.rol.nombre == 'Admin':
                return True
            else:
                return request.user.rol.nombre in self.roles_required
            # any(role in self.roles_required for role in request.user.roles)
        return False
