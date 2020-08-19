from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'users_app'

    def ready(self):
      from . signals import send_welcome_email
