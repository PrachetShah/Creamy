from django.apps import AppConfig

# Register this app in settings.py
# home.apps.HomeConfig(i.e Class name)
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
