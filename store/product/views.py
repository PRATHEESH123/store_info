# 3rd party
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# django filter
from django_filters.rest_framework import DjangoFilterBackend

# local
from .models import Category ,Product
from .serializers import CategorySerializer,ProductSerializer



class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ['sub_category','category']
    search_fields = ['name']