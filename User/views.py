from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from User.models import User
from User.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
       
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]  # Only authenticated users can list/retrieve users
        elif self.action == 'create':
            permission_classes = [AllowAny]  # Anyone can create a new user
        else:
            permission_classes = [IsAuthenticated]  # Update/delete require authentication
        return permission_classes

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
