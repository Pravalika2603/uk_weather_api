from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Region(models.Model):
    """Model for UK regions"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class WeatherParameter(models.Model):
    """Model for weather parameters (Tmax, Tmin, etc.)"""
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)
    unit = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.unit})"

    class Meta:
        ordering = ['name']


class WeatherData(models.Model):
    """Main model for storing weather data"""
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='weather_data')
    parameter = models.ForeignKey(
        WeatherParameter, on_delete=models.CASCADE, related_name='weather_data')
    year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2030)])
    month = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(12)], null=True, blank=True)
    value = models.FloatField()
    is_provisional = models.BooleanField(default=False)
    data_source_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('region', 'parameter', 'year', 'month')
        ordering = ['-year', '-month']

    def __str__(self):
        month_str = f"/{self.month:02d}" if self.month else ""
        return f"{self.region.name} - {self.parameter.name} - {self.year}{month_str}: {self.value}"
