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

def test_api_view(request):
    students = requests.get("https://attendance-ghip.onrender.com/students/").json()
    return JsonResponse({"students": students})
