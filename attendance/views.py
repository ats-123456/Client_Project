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
#___________________________________old________________________________________
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']

#             try:
#                 user = Staff.objects.get(username=username)
#                 if check_password(password, user.password):
#                     # Generate JWT token
#                     refresh = RefreshToken.for_user(user)
                    
#                     data = {
#                         'message': 'Login successful',
#                         'username': user.username,
#                         'role': user.role,
#                         'user_id': user.s_id,
#                         'staff_id': user.staff_id,
#                         'hod_id': user.hod_id,
#                         'access_token': str(refresh.access_token),
#                         'refresh_token': str(refresh)
#                     }
#                     return Response(data, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
#             except Staff.DoesNotExist:
#                 return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#_______________________________old______________________________________________________
# 
# __________________________________new_____________________________________________
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Staff
from .serializers import LoginSerializer

class StaffLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = Staff.objects.get(username=username)
                if user.check_password(password):  # Uses your custom check_password method
                    # Manually create a token for this custom user
                    refresh = RefreshToken()
                    refresh['username'] = user.username
                    refresh['s_id'] = user.s_id
                    refresh['role'] = user.role

                    return Response({
                        'message': 'Login successful',
                        'username': user.username,
                        'user_id': user.s_id,
                        'role': user.role,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                        'staff_id': user.staff_id,
                        'hod_id': user.hod_id
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Staff.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#__________________________________________new___ 

from .models import StaffAssignment
from .serializers import StaffAssignmentSerializer

  
from .models import StaffAssignment
from .serializers import StaffAssignmentSerializer
from rest_framework import viewsets

# class StaffAssignmentViewSet(viewsets.ModelViewSet):
#     serializer_class = StaffAssignmentSerializer
    
#     def get_queryset(self):
#         s_id = self.request.query_params.get('s_id')  # Use 'id' query parameter for filtering
#         print(s_id)
#         if s_id:
#             # Filter by the related staff's 's_id' field, not the 'id' of StaffAssignment
#             return StaffAssignment.objects.filter(staff__s_id=s_id)  # Filter by related staff's s_id

#         return StaffAssignment.objects.all()






# class StaffAssignmentViewSet(viewsets.ModelViewSet):
#     serializer_class = StaffAssignmentSerializer

#     def get_queryset(self):
#         user = self.request.user
#         print("Logged-in user:", user)

#         # Only return assignments related to the logged-in staff user
#         return StaffAssignment.objects.filter(staff__s_id=user.s_id)





# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user_data(request):
#     user = request.user  # JWT token la irukura user
#     return Response({
#         'username': user.username,
#         'email': user.email,
#         'id': user.id,
#         'is_staff': user.is_staff,
#     })

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Staff
from rest_framework import status

# class StaffAssignmentViewSet(viewsets.ModelViewSet):
#    serializer_class = StaffAssignmentSerializer

#    def get_queryset(self):
#         s_id = self.request.query_params.get('s_id')

#         if s_id is not None:
#             try:
#                 s_id = int(s_id)
#                 r=StaffAssignment.objects.filter(staff__s_id=s_id)
#                 for i in  r:
#                     s_id=i.staff.s_id
#                     name=i.staff.username
#                     rol=i.staff.role
#                     sid=i.staff.staff_id
#                     hid=i.staff.hod_id
#                     classn=i.assigned_class

#                 print(name,rol,sid,hid)

#                 # return StaffAssignment.objects.filter(staff__s_id=s_id)
#                 return Response({
#                      's_id':s_id,
#                      'classname':classn,
                        
#                         'username': name,
#                         'role': rol,
                      
#                         'staff_id': sid,
#                         'hod_id': hid,



#                     }, status=status.HTTP_200_OK)
            
#             except ValueError:
#                 return StaffAssignment.objects.none()  # Or raise a validation error

#         return StaffAssignment.objects.all()


from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import StaffAssignment
from .serializers import StaffAssignmentSerializer

class StaffAssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = StaffAssignmentSerializer

    def get_queryset(self):
        # Return the basic queryset here
        s_id = self.request.query_params.get('s_id')
        if s_id is not None:
            try:
                s_id = int(s_id)
                return StaffAssignment.objects.filter(staff__s_id=s_id)
            except ValueError:
                return StaffAssignment.objects.none()
        return StaffAssignment.objects.all()

    def list(self, request, *args, **kwargs):
        s_id = self.request.query_params.get('s_id')
        if s_id is not None:
            try:
                s_id = int(s_id)
                assignments = StaffAssignment.objects.filter(staff__s_id=s_id)
                if assignments.exists():
                    staff = assignments.first().staff  # Get staff details once
                    class_list = [str(assign.assigned_class) for assign in assignments]

                    return Response({
                        's_id': staff.s_id,
                        'username': staff.username,
                        'role': staff.role,
                        'staff_id': str(staff.staff_id),
                        'hod_id': str(staff.hod_id),
                        'classes': class_list  # all class names
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'No assignment found'}, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                return Response({'error': 'Invalid s_id'}, status=status.HTTP_400_BAD_REQUEST)

        # Default behavior
        return super().list(request, *args, **kwargs)







from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Year
from .serializers import StudentSerializer

class StudentsByClassView(APIView):
    def get(self, request):
        class_id = request.query_params.get('class_id')
        if class_id is not None:
            try:
                year_obj = Year.objects.get(id=class_id)
                students = Student.objects.filter(class_info=year_obj)
                serializer = StudentSerializer(students, many=True)
                return Response({
                    'class': str(year_obj),
                    'total_students': students.count(),
                    'students': serializer.data
                }, status=status.HTTP_200_OK)
            except Year.DoesNotExist:
                return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'class_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

#http://127.0.0.1:8000/api/students-by-class/?class_id=1
#GET /students-by-class/?class_id=<year_id>









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




