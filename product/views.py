from rest_framework import generics

from .models import Category, Image, Product
from .serializers import (
    CategorySerializer,
    ImageSerializer,
    ProductFormSerializer,
    UnregisteredProductSerializer,
)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UnregisteredProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = UnregisteredProductSerializer
    authentication_classes = []
    permission_classes = []


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductFormSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductFormSerializer
    queryset = Product.objects.all()
