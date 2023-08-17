from django.urls import path

from .views import UserListAPIView, UserSignUpView, UserByTokenView


urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="users"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("token/user/", UserByTokenView.as_view(), name="token_user"),
]
