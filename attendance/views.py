from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


from django.http import JsonResponse
import requests

# attendance/views.py

from attendance.models import Student  # or from the view logic directly
from attendance.serializers import StudentSerializer
from django.http import JsonResponse

def test_api_view(request):
    students = Student.objects.all()
    serialized = StudentSerializer(students, many=True)
    return JsonResponse(serialized.data, safe=False)



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
