from django.apps import AppConfig


class MembersConfig(AppConfig):
    """
    Configuration class for the 'members' app.

    Attributes:
        default_auto_field (str): The default auto field to use for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
