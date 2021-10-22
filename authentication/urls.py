from django.urls import path
from .views import RegisterView, LoginAPIView


urlpatterns = [
    path('signup/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login")
]
