from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    AppConfig for the 'pages' app.

    Attributes:
        default_auto_field (str): The default auto-generated field for models.
        name (str): The name of the app.

    Example:
        To use this AppConfig, add the following in the app's apps.py file:

        ```python
        from django.apps import AppConfig

        class PagesConfig(AppConfig):
            default_auto_field = 'django.db.models.BigAutoField'
            name = 'pages'
        ```
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
