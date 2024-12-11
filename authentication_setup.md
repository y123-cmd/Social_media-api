# Authentication Setup for Social Media API

This document explains how to set up authentication for the Social Media API using Django REST Framework and JWT (JSON Web Tokens).

## Required Packages

Make sure you have the following packages installed:

- `djangorestframework` - Django REST Framework to build the API.
- `djangorestframework-simplejwt` - For JWT authentication.
- `django` - For the base Django setup.

You can install them using pip:

```bash
pip install djangorestframework djangorestframework-simplejwt
Django Settings
Update settings.py
Add rest_framework and rest_framework_simplejwt to the INSTALLED_APPS:


INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]
Configure authentication in the REST_FRAMEWORK settings:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
Endpoints for Authentication
1. POST /register/: Register a new user
Request body (JSON):
json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
Response:
Success: User created successfully (status code: 201)
Error: User already exists (status code: 400)
2. POST /login/: Login and receive a JWT token
Request body (JSON):
json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
Response:
Success: Access and Refresh tokens
Error: Invalid credentials (status code: 400)
json
Copy code
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
Testing Authentication Endpoints
You can test the authentication endpoints using tools like Postman or curl.

Testing the /register/ Endpoint
POST request to /register/ with the body:
json
Copy code
{
  "username": "testuser",
  "password": "testpassword"
}
Response:
json
Copy code
{
  "message": "User created successfully"
}
Testing the /login/ Endpoint
POST request to /login/ with the body:
json
Copy code
{
  "username": "testuser",
  "password": "testpassword"
}
Response:
json
Copy code
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
Conclusion
This setup provides basic user authentication using Django REST Framework with JWT tokens. The register and login endpoints allow users to create accounts and authenticate using tokens. You can use Postman or curl to test these authentication endpoints.

vbnet
Copy code

### Step 2: Add the file to your GitHub repository

1. After creating the `authentication_setup.md` file, save it in your project's root directory or wherever you keep documentation files (e.g., `/docs` folder).

2. Now, open your terminal (in the root directory of your project) and run the following Git commands to add, commit, and push the file to your repository:

```bash
# Add the file to the staging area
git add authentication_setup.md

# Commit the change
git commit -m "Add authentication setup documentation"

# Push the change to the remote repository
git push origin capstone-features
This will upload the authentication_setup.md file to your GitHub repository.










