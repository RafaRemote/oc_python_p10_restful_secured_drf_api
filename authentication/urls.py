from django.urls import path
from .views import RegisterView, LogoutAPIView, LoginAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
