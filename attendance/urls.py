from rest_framework import routers
from .views import StudentViewSet, AttendanceViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = router.urls
