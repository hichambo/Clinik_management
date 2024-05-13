from rest_framework import serializers
from medications.models import Medication
from User.serializers import UserSerializer

class MedicationSerializer(serializers.ModelSerializer):
    prescribed_by = UserSerializer(read_only=True)  # Nested prescribing provider (read-only)
    patient = UserSerializer(read_only=True)  # Nested patient information (read-only)

    class Meta:
        model = Medication
        fields = ('id', 'name', 'dosage', 'instructions', 'prescribed_by', 'patient')
