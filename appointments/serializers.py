from rest_framework import serializers
from appointments.models import Appointment
from User.serializers import UserSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True)  # Nested patient information (read-only)
    provider = UserSerializer(read_only=True)  # Nested provider information (read-only)

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'provider', 'date_time')
