from django.urls import path
from .views import RegisterView, LoginAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('login2/', jwt_views.TokenObtainPairView.as_view(), name='login2')

]
