from rest_framework.permissions import BasePermission

def RolePermissionFactory(allowed_roles):
    class RolePermission(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.role in allowed_roles
    return RolePermission

"""
RolePermissionFactory → Dynamically creates a DRF permission class.

Checks if the user is authenticated and has an allowed role.

Makes role-based access control flexible and reusable.

"""