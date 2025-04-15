from rest_framework import routers
from .views import StudentViewSet, AttendanceViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = router.urls
from django.urls import path
from . import views

urlpatterns = [
    path("test-api/", views.test_api_view),
     path('register/', views.register_user, name='register_user'),
] + router.urls
