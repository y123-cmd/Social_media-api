

from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_list, name='profile_list'),  # For profile list
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),  # For profile detail
]

