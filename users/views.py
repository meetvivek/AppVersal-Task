from django.shortcuts import render
from .models import Image
from .serializers import RegisterSerializer, ImageUploadSerializer, ReadOnlyImageSerializer
from rest_framework import generics, permissions
from .bg_task import image_operation
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ImageUploadView(generics.CreateAPIView):
    serializer_class = ImageUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, file_name=self.request.FILES['image'].name)
        image_operation(serializer.instance.id)


class UserImageView(generics.ListAPIView):
    serializer_class = ReadOnlyImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user).values('file_name')