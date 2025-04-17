from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = router.urls
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [ 
    path('register/', views.register_user, name='register_user'),
    path('login/', views.StaffTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls




