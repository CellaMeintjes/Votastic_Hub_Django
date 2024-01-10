from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    AppConfig for the 'blog' app.

    This class defines the configuration for the 'blog' app. It includes
    settings such as the default auto field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
