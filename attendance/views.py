from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import UserRegistrationSerializer, UserProfileSerializer

#___________________________________________________________________________
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Staff
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = Staff.objects.get(username=username)
                if check_password(password, user.password):
                    # Generate JWT token
                    refresh = RefreshToken.for_user(user)
                    
                    data = {
                        'message': 'Login successful',
                        'username': user.username,
                        'role': user.role,
                        'user_id': user.s_id,
                        'staff_id': user.staff_id,
                        'hod_id': user.hod_id,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh)
                    }
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Staff.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .models import StaffAssignment
from .serializers import StaffAssignmentSerializer

  
from .models import StaffAssignment
from .serializers import StaffAssignmentSerializer
from rest_framework import viewsets

class StaffAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = StaffAssignmentSerializer
    
    def get_queryset(self):
        s_id = self.request.query_params.get('s_id')  # Use 'id' query parameter for filtering
        print(s_id)
        if s_id:
            # Filter by the related staff's 's_id' field, not the 'id' of StaffAssignment
            return StaffAssignment.objects.filter(staff__s_id=s_id)  # Filter by related staff's s_id

        return StaffAssignment.objects.all()













#_____________________________________________________________________________

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         user_serializer = UserRegistrationSerializer(data=request.data)
#         if user_serializer.is_valid():
#             user = user_serializer.save()
#             profile_data = request.data.get('profile')
#             if profile_data:
#                 profile_serializer = UserProfileSerializer(data=profile_data)
#                 if profile_serializer.is_valid():
#                     profile_serializer.save(user=user)
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.exceptions import AuthenticationFailed


# class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
        
#         if not self.user.is_staff:
#             raise AuthenticationFailed("You are not authorized to login. Contact Admin.")

#         return data

# class StaffTokenObtainPairView(TokenObtainPairView):
#     serializer_class = StaffTokenObtainPairSerializer


