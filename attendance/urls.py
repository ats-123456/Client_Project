from rest_framework import routers


router = routers.DefaultRouter()



from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router.register(r'staff-assignments', views.StaffAssignmentViewSet, basename='staff-assignment')
urlpatterns = [ 
    # path('register/', views.register_user, name='register_user'),
    # path('login/', views.StaffTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('login/',views.LoginView.as_view(), name='login'),
    #  path('staff-assignments/',views.StaffAssignmentViewSet.as_view(),name='staff-assignments')

    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls




