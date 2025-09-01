from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .models import Region, WeatherParameter, WeatherData
from .serializers import RegionSerializer, WeatherParameterSerializer, WeatherDataSerializer


class StandardPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = StandardPagination


class WeatherParameterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherParameter.objects.all()
    serializer_class = WeatherParameterSerializer
    pagination_class = StandardPagination


class WeatherDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherData.objects.select_related('region', 'parameter')
    serializer_class = WeatherDataSerializer
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'region__code': ['exact'],
        'parameter__code': ['exact'],
        'year': ['exact', 'gte', 'lte'],
        'month': ['exact', 'gte', 'lte'],
    }


def home(request):
    return render(request, 'home.html')
