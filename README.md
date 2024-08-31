# AppVersal - Sample Task (Django)

## Project Overview

This Django project provides a RESTful API for managing user registration and image processing. The key features of the project include:

- **User Management**: Register new users with basic details including username, email, password, name, age and location.
- **Image Upload**: Users can upload images which are automatically processed to convert them to black and white.
- **Image Retrieval**: Users can view a list of their uploaded images and retrieve the filenames.

## Endpoints

- **Register User**: `/task/register/`
  - **Method**: `POST`
  - **Description**: Register a new user with the specified details.

- **Upload Image**: `/task/upload/`
  - **Method**: `POST`
  - **Description**: Upload an image file. The image will be converted to black and white.

- **Retrieve Image**: `/task/images/`
  - **Method**: `GET`
  - **Description**: Retrieve the images uploaded by the authenticated user.
