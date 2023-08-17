from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, views

from .serializers import UserSerializer, UserSignUpSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer


class UserByTokenView(views.APIView):
    def get(self, request, *args, **kwargs):
        userSerializer = UserSerializer(request.user)
        return JsonResponse(userSerializer.data)
