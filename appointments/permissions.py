from rest_framework.permissions import BasePermission

from appointments.models import Appointment

class IsAuthenticatedUser(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class IsAdminOrPatient(BasePermission):
    """
    Allows access only to admins or the patient associated with the appointment.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:  # For list, retrieve, update, delete
            appointment_id = view.kwargs.get('pk')  # Get appointment ID from URL parameters
            if appointment_id:
                try:
                    appointment = Appointment.objects.get(pk=appointment_id)
                    return (request.user.is_authenticated and
                            (request.user.is_admin or appointment.patient == request.user))
                except Appointment.DoesNotExist:
                    return False
        return request.user and request.user.is_authenticated  # Fallback for other methods
