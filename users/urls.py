from django.urls import path
from .views import RegisterView, ImageUploadView, UserImageView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('upload/', ImageUploadView.as_view(), name='image_upload'),
    path('images/', UserImageView.as_view(), name='user-image-names'),
]
