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

