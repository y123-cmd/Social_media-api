
# Social Media API
This is the backend API for a Social Media platform. It allows users to manage profiles, posts, comments, and user authentication. The project is built using Django and Django REST Framework.

## Setup Instructions

Follow these steps to set up the development environment:

1. **Create a virtual environment**:  
   In your project folder, run the following command to create a virtual environment:
   ```bash
   python -m venv venv
2.pip install django djangorestframework
3.django-admin startproject socialmedia
4.python manage.py startapp users
5.INSTALLED_APPS = [
    # Other default apps...
    'rest_framework',  # Django REST Framework
    'users',  # Your app
]
6.python manage.py runserver


