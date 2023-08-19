import django_filters
from .choices import PRODUCT_STATUS
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.ChoiceFilter(choices=PRODUCT_STATUS)
    categories = django_filters.CharFilter(method="filter_categories")

    def filter_categories(self, queryset, name, value):
        categories = value.split(",") if value else []
        return queryset.filter(categories__id__in=categories)

    class Meta:
        model = Product
        fields = []
