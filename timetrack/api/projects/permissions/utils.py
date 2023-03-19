from django.conf import settings


def is_superuser(user: settings.AUTH_USER_MODEL) -> bool:
    return user.is_authenticated and user.is_superuser
