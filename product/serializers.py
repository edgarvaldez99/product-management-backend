from rest_framework import serializers

from .choices import PRODUCT_STATUS, INACTIVE
from .fields import HttpBase64ImageField
from .models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(read_only=True)

    def get_queryset(self):
        return Category.objects.all()

    class Meta:
        model = Category
        fields = ["id", "name"]


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    photo = HttpBase64ImageField()

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
    categories = CategorySerializer(many=True)
    images = ImageSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        categories = validated_data.pop("categories", [])
        images = validated_data.pop("images", [])
        product = Product.objects.create(**validated_data)
        product.categories.set(
            [Category.objects.get(pk=category.get("id")) for category in categories]
        )
        product.images.set(
            [Image.objects.create(photo=dict(image).get("photo")) for image in images]
        )
        return product

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.status = validated_data.get("status", instance.status)
        categories = validated_data.get("categories", instance.categories)
        instance.categories.set(
            [Category.objects.get(pk=category.get("id")) for category in categories]
        )
        images = validated_data.get("images", None)
        if images:
            instance.images.set(
                [
                    Image.objects.create(photo=dict(image).get("photo"))
                    for image in images
                ]
            )
        instance.save()
        return instance
