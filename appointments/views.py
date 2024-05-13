from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAdminOrPatient
from rest_framework.response import Response
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from User.models import User
from .permissions import IsAdminOrPatient

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        """
        Define permissions based on view action.
        """
        if self.action in ['list']:
            # Authenticated users can view filtered appointments based on user type
            permission_classes = [IsAuthenticated]
        else:
            # Other actions require specific permissions
            permission_classes = self.get_action_permissions()
        return permission_classes

    def get_action_permissions(self):
        """
        Define permissions for specific view actions.
        """
        permissions = {
            'retrieve': [IsAdminOrPatient],
            'create': [IsAuthenticated],
            'update': [IsAdminOrPatient],
            'destroy': [IsAdminUser],
        }
        return permissions.get(self.action, [])

    def get_queryset(self):
        """
        Filter appointments based on user type (for list action).
        """
        user = self.request.user
        if user.is_authenticated:
            if user.user_type == 'patient':
                return Appointment.objects.filter(patient=user)
            elif user.user_type == 'provider':
                return Appointment.objects.filter(provider=user)
        return Appointment.objects.none()  # Admins see all (handled by permissions)
