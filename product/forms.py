from django import forms
from .models import Category, Image, Product


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)


class ImageAdminForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("photo",)


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "status", "categories", "images")
