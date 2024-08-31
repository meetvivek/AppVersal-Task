from rest_framework import serializers
from .models import CustomUser, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'name', 'age', 'location')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'name', 'age', 'location')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'file_name', 'uploaded_at']


class ReadOnlyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file_name']