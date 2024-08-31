from PIL import Image as PILImage
from io import BytesIO
from .models import Image
from django.core.files.base import ContentFile

def image_operation(image_id):
    try:
        image_instance = Image.objects.get(id=image_id)
        image_file = image_instance.image

        if not image_file:
            raise ValueError("Error: No image file found.")

        image = PILImage.open(image_file)
        image_bw = image.convert("L")
        
        buffer = BytesIO()
        image_bw.save(buffer, format='JPEG')
        buffer.seek(0)
        new_image_file = ContentFile(buffer.read(), name=image_file.name)

        image_instance.image.save(image_file.name, new_image_file, save=True)

    except Image.DoesNotExist:
        print("Image not found.")

    except ValueError as xyz:
        print(f"Error processing image: {xyz}")
