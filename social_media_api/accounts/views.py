from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET', 'POST'])
def profile_list(request):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Check if a profile already exists for the user
        user_id = request.data.get('user')
        if Profile.objects.filter(user_id=user_id).exists():
            return Response({"error": "This user already has a profile."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Ensure the user is authenticated
    if request.user.is_authenticated:
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Authentication views (Newly added views)

class RegisterView(APIView):
    def post(self, request):
        # Register a new user
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        # Login and return JWT tokens
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Check if the user exists and validate the password
        user = User.objects.filter(username=username).first()
        if not user or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
