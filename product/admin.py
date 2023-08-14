from django.contrib import admin

from .forms import CategoryAdminForm, ImageAdminForm, ProductAdminForm
from .models import Category, Image, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["id", "name"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = ["photo"]
    search_fields = ["photo"]
    ordering = ["id", "photo"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "status")
    search_fields = ["name", "status", "categories", "images"]
    ordering = ["id", "name", "status"]
