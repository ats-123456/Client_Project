from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = router.urls
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [ 
     path('register/', views.register_user, name='register_user'),
      path('register_staff/',views.RegisterView.as_view(), name='register_staff'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
