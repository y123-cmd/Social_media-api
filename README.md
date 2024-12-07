# Social Media API

This is the backend API for a **Social Media Platform**. It allows users to manage profiles, posts, comments, and user authentication. The project is built using **Django** and **Django REST Framework** (DRF).

## Setup Instructions

Follow these steps to set up the development environment:

### 1. **Create a Virtual Environment**
In your project folder, run the following command to create a virtual environment:

```bash
python -m venv venv
2. Install the Django REST Framework
In your project folder, run the following command to install Django and Django REST Framework (DRF):

bash
Copy code
pip install django djangorestframework
3. Create a New Django Project
Create a new Django project by running:

bash
Copy code
django-admin startproject socialmedia
4. Create a New Django App
Create a new Django app (for handling user profiles, posts, and comments) by running:

bash
Copy code
cd socialmedia
python manage.py startapp users
5. Add the App to the Project
Open socialmedia/settings.py and add 'users' and 'rest_framework' to the INSTALLED_APPS list:

python
Copy code
INSTALLED_APPS = [
    # Other default apps...
    'rest_framework',  # Django REST Framework
    'users',  # Your app
]
6. Set Up the Database
Run the migrations to set up the initial database structure:

bash
Copy code
python manage.py migrate
