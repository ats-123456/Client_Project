from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer, UserProfileSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        user_serializer = UserRegistrationSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile_data = request.data.get('profile')
            if profile_data:
                profile_serializer = UserProfileSerializer(data=profile_data)
                if profile_serializer.is_valid():
                    profile_serializer.save(user=user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
