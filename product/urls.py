from rest_framework import routers

from .views import CategoryViewSet, ImageViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"images", ImageViewSet)
router.register(r"products", ProductViewSet)
