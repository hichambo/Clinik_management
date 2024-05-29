from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from diets.models import DietPlan
from diets.serializers import DietPlanSerializer

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer
    permission_classes = [IsAuthenticated]  # Base permission for all actions

    def get_queryset(self):
        """
        Filter diet plans to the currently authenticated user (if not an admin).
        """
        user = self.request.user
        if not user.is_staff:
            return self.queryset.filter(patient=user)
        return self.queryset  # Admins see all diet plans

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

    def get_permissions(self):
        """
        Define permissions based on view action.
        """
        if self.action in ['destroy']:
            permission_classes = [IsAdminUser]  # Only admins can delete diet plans
        else:
            permission_classes = self.permission_classes
        return permission_classes
