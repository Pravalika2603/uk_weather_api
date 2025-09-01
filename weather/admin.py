from django.contrib import admin
from .models import Region, WeatherParameter, WeatherData


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description', 'created_at']
    search_fields = ['name', 'code']


@admin.register(WeatherParameter)
class WeatherParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'unit', 'description']
    search_fields = ['name', 'code']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['region', 'parameter', 'year',
                    'month', 'value', 'is_provisional']
    list_filter = ['region', 'parameter', 'year', 'is_provisional']
    search_fields = ['region__name', 'parameter__name']
