from django.urls import path

from .views import (
    CategoryListCreateAPIView,
    ImageListCreateAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    UnregisteredProductListAPIView,
)


urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view(), name="categories"),
    path("images/", ImageListCreateAPIView.as_view(), name="images"),
    path("products/", ProductListCreateAPIView.as_view(), name="products"),
    path(
        "products/<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="products_update",
    ),
    path(
        "products/unregistered/",
        UnregisteredProductListAPIView.as_view(),
        name="products_unregistered",
    ),
]
