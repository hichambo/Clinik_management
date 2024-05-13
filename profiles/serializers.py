from rest_framework import serializers
from profiles.models import Profile
from User.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user information (read-only)

    class Meta:
        model = Profile
        fields = ('user', 'date_of_birth', 'diabetes_type')
