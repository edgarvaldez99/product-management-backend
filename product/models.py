from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import PRODUCT_STATUS, INACTIVE


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Image(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    status = models.CharField(
        max_length=50,
        verbose_name=_("status"),
        choices=PRODUCT_STATUS,
        default=INACTIVE,
    )
    categories = models.ManyToManyField(Category, verbose_name=_("categories"))
    images = models.ManyToManyField(Image, verbose_name=_("images"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
