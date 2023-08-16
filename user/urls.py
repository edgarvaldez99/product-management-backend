from django.urls import path

from .views import UserListAPIView, UserSignUpView


urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="users"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
]
