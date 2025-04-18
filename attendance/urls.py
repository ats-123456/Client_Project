from rest_framework import routers





# from django.urls import path
# from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# router.register(r'staff-assignments', views.StaffAssignmentViewSet, basename='staff-assignment')
# urlpatterns = [ 
#     # path('register/', views.register_user, name='register_user'),
#     # path('login/', views.StaffTokenObtainPairView.as_view(), name='token_obtain_pair'),
#      path('login/',views.StaffLoginView.as_view(), name='login'),

#     #  path('user/',views.get_user_data, name='get_user_data'),
#     #  path('staff-assignments/',views.StaffAssignmentViewSet.as_view(),name='staff-assignments')

#     # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ] + router.urls



# from django.urls import path
# from .views import StaffLoginView,StaffUserDataView
# from rest_framework_simplejwt.views import TokenRefreshView

# urlpatterns = [
#     path('staff-login/', StaffLoginView.as_view(), name='staff-login'),
#          path('user/', StaffUserDataView.as_view(), name='get-user-data'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffLoginView, StaffAssignmentViewSet

router = DefaultRouter()
router.register(r'staff-assignments', StaffAssignmentViewSet, basename='staff-assignment')

urlpatterns = [
    path('login/', StaffLoginView.as_view(), name='staff-login'),
    path('', include(router.urls)),
]
