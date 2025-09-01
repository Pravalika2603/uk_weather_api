from django.core.management.base import BaseCommand
from weather.parsers import MetOfficeDataParser, initialize_default_data
from weather.models import Region, WeatherParameter


class Command(BaseCommand):
    help = 'Fetch weather data from UK MetOffice and initialize default data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--init',
            action='store_true',
            help='Initialize default regions and parameters',
        )

    def handle(self, *args, **options):
        if options['init']:
            self.stdout.write('Initializing default data...')
            initialize_default_data()
            self.stdout.write(self.style.SUCCESS('Default data initialized'))

            # Show what was created
            regions = Region.objects.all()
            parameters = WeatherParameter.objects.all()

            self.stdout.write(
                f'Regions: {", ".join([r.name for r in regions])}')
            self.stdout.write(
                f'Parameters: {", ".join([p.name for p in parameters])}')
        else:
            self.stdout.write(
                'Use --init flag to initialize default regions and parameters')
            self.stdout.write(
                'Example: python manage.py fetch_weather_data --init')
