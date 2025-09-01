import requests
from datetime import datetime
from .models import Region, WeatherParameter, WeatherData


class MetOfficeDataParser:
    """Parser for UK MetOffice regional series data"""

    BASE_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Weather-Data-API/1.0'
        })

    def get_data_url(self, parameter: str, region: str, order_type: str = 'date'):
        """Generate URL for MetOffice data file"""
        return f"{self.BASE_URL}/{parameter}/{order_type}/{region}.txt"

    def fetch_data_file(self, url: str):
        """Fetch data file content from URL"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None


def initialize_default_data():
    """Initialize default regions and weather parameters"""

    # Default regions (add more if not already present)
    regions = [
        {'name': 'United Kingdom', 'code': 'UK', 'description': 'Whole of the UK'},
        {'name': 'England', 'code': 'England', 'description': 'England'},
        {'name': 'Wales', 'code': 'Wales', 'description': 'Wales'},
        {'name': 'Scotland', 'code': 'Scotland', 'description': 'Scotland'},
    ]

    for region_data in regions:
        Region.objects.get_or_create(
            code=region_data['code'],
            defaults={
                'name': region_data['name'],
                'description': region_data['description']
            }
        )

    # Default weather parameters (add more if not already present)
    parameters = [
        {'name': 'Maximum Temperature', 'code': 'Tmax', 'unit': '°C',
            'description': 'Mean daily maximum temperature'},
        {'name': 'Minimum Temperature', 'code': 'Tmin', 'unit': '°C',
            'description': 'Mean daily minimum temperature'},
        {'name': 'Precipitation', 'code': 'Rainfall',
            'unit': 'mm', 'description': 'Total precipitation'},
    ]

    for param_data in parameters:
        WeatherParameter.objects.get_or_create(
            code=param_data['code'],
            defaults={
                'name': param_data['name'],
                'unit': param_data['unit'],
                'description': param_data['description']
            }
        )
