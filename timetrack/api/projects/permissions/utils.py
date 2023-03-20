from django.conf import settings


def is_superuser(user: settings.AUTH_USER_MODEL) -> bool:
    """
    Checks whether a user is a superuser.
    """
    return user.is_authenticated and user.is_superuser
