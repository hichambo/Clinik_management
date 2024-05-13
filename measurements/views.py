from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Measurement
from .serializers import MeasurementSerializer

from django.utils import mixins # For DRY filtering


class MeasurementViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView, mixins.UserObjectMixin):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter measurements to the currently authenticated user.
        """
        return self.get_user_objects(queryset=super().get_queryset())

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
