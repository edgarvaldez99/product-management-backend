from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .choices import PRODUCT_STATUS, INACTIVE
from .models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    photo = Base64ImageField()

    def get_queryset(self):
        return Image.objects.all()

    class Meta:
        model = Image
        fields = ["id", "photo"]


class UnregisteredProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "status"]


class ProductFormSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.ChoiceField(
        choices=PRODUCT_STATUS,
        default=INACTIVE,
    )
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )
    images = ImageSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        categories = validated_data.pop("categories", [])
        images = validated_data.pop("images", [])
        product = Product.objects.create(**validated_data)
        product.categories.set(categories)
        product.images.set([Image.objects.create(**image) for image in images])
        return product

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.status = validated_data.get("status", instance.status)
        instance.categories.set(validated_data.get("categories", instance.categories))
        images = validated_data.get("images", instance.images)
        instance.images.set([Image.objects.create(**image) for image in images])
        instance.save()
        return instance
