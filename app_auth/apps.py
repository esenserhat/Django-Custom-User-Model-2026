from django.apps import AppConfig


class AppAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_auth'
    verbose_name = 'User Management System'
    main_url = '/app-auth/'
    description = 'User Management System for handling user accounts, authentication, and profile management.'