from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from User.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        """
        Define permissions based on view action.
        """
        if self.action in ['retrieve', 'update']:
            # Only authenticated users can view or update their profile
            permission_classes = [IsAuthenticated]
        else:
            # Deny access for other actions (create, delete, list)
            permission_classes = []
        return permission_classes

    def get_queryset(self):
        """
        Filter profiles to the currently authenticated user.
        """
        user = self.request.user
        if user.is_authenticated:
            return Profile.objects.filter(user=user)
        return Profile.objects.none()  # No profile for unauthenticated users

    def perform_create(self, serializer):
        """
        Override create to associate the profile with the requesting user.
        """
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            raise PermissionError('You need to be logged in to create a profile.')
