from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, views

from .serializers import UserSerializer, UserSignUpSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer
    authentication_classes = []
    permission_classes = []


class UserByTokenView(views.APIView):
    def get(self, request, *args, **kwargs):
        userSerializer = UserSerializer(request.user)
        user = {
            "id": userSerializer.data.get("id"),
            "username": userSerializer.data.get("username"),
            "firstName": userSerializer.data.get("first_name"),
            "lastName": userSerializer.data.get("last_name"),
            "email": userSerializer.data.get("email"),
            "isActive": userSerializer.data.get("is_active"),
        }
        return JsonResponse(user)
