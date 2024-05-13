from rest_framework import serializers
from measurements.models import Measurement
from User.serializers import UserSerializer

class MeasurementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user information (read-only)

    class Meta:
        model = Measurement
        fields = ('id', 'user', 'date_time', 'type', 'value', 'condition_type')
