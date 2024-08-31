from django.urls import path
from .views import RegisterView, ImageUploadView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('upload/', ImageUploadView.as_view(), name='image_upload'),
]
