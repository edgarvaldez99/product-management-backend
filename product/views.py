from django.views.generic.detail import SingleObjectMixin
from rest_framework import generics

from .filters import ProductFilter
from .models import Category, Image, Product
from .permissions import IsActiveUser
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
    filterset_class = ProductFilter


class ProductMixin(SingleObjectMixin):
    serializer_class = ProductFormSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductListCreateAPIView(ProductMixin, generics.ListCreateAPIView):
    filterset_class = ProductFilter


class ProductRetrieveUpdateDestroyAPIView(
    ProductMixin, generics.RetrieveUpdateDestroyAPIView
):
    pass
