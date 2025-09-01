# UK Weather Data API

A Django REST API application for UK MetOffice weather data.

## Features

- REST API endpoints for weather data
- Django admin interface for data management
- Frontend dashboard
- Docker support
- SQLite database

## Installation

1. Clone the repository
2. Create virtual environment: `python3 -m venv weather_env`
3. Activate: `source weather_env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Initialize data: `python manage.py fetch_weather_data --init`
8. Run server: `python manage.py runserver`

## API Endpoints

- `/api/regions/` - List UK regions
- `/api/parameters/` - List weather parameters
- `/api/weather-data/` - Weather data with filtering
- `/admin/` - Django admin panel

## Usage

Visit `http://127.0.0.1:8000/` for the dashboard.

## Technologies

- Django 4.2
- Django REST Framework
- SQLite
- Docker

## Assignment Requirements

- Project Setup ✓
- Data Parsing ✓
- Data Modeling ✓
- REST API ✓
- Frontend ✓
- Docker ✓
- Git Workflow ✓
