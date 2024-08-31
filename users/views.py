from django.shortcuts import render
from .models import Image
from .serializers import RegisterSerializer, ImageUploadSerializer
from rest_framework import generics, permissions
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ImageUploadView(generics.CreateAPIView):
    serializer_class = ImageUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, file_name=self.request.FILES['image'].name)
