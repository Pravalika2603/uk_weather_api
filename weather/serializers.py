from rest_framework import serializers
from .models import Region, WeatherParameter, WeatherData


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'code', 'description', 'created_at']


class WeatherParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherParameter
        fields = ['id', 'name', 'code', 'unit', 'description', 'created_at']


class WeatherDataSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    parameter = WeatherParameterSerializer(read_only=True)

    class Meta:
        model = WeatherData
        fields = [
            'id', 'region', 'parameter', 'year', 'month', 'value',
            'is_provisional', 'data_source_url', 'created_at', 'updated_at'
        ]
