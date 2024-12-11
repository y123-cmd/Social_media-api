from django.urls import path
from . import views
from .views import RegisterView, LoginView

urlpatterns = [
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),  # For user registration
    path('login/', LoginView.as_view(), name='login'),  # For user login
    
    # Profile-related URLs
    path('profile/', views.profile_list, name='profile_list'),  # For profile list (GET) and creating a profile (POST)
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),  # For profile detail (GET, PUT, DELETE)
]
