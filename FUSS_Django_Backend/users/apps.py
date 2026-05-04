from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Connects signal to be activated.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        import users.signals
