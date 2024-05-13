from rest_framework.permissions import BasePermission

class IsAuthenticatedUser(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class IsPatient(BasePermission):
    """
    Allows access only to users with the "patient" user type.
    """
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'patient'

class IsProvider(BasePermission):
    """
    Allows access only to users with the "provider" user type.
    """
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'provider'
