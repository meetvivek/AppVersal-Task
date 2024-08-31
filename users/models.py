from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=300,  blank=True, null=True)

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_images')
    image = models.ImageField(upload_to='user_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255, blank=True)
