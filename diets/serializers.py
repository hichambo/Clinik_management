from rest_framework import serializers
from diets.models import DietPlan
from User.serializers import UserSerializer

class DietPlanSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)  # Nested creator provider (read-only)
    patient = UserSerializer(read_only=True)  # Nested patient information (read-only)

    class Meta:
        model = DietPlan
        fields = ('id', 'description', 'recommendations', 'created_by', 'patient')
