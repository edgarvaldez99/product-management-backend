from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import UserSerializer, UserSignUpSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
