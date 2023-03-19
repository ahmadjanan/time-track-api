from django.conf import settings
from factory.django import DjangoModelFactory


class TimeTrackUserFactory(DjangoModelFactory):
    """
    User Factory for generating test TimeTrackUser instances in database.
    """
    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ("email",)

    email = "test@example.com"
    username = "test"
    first_name = "Test"
    last_name = "User"

    @staticmethod
    def with_password(password, **kwargs):
        """
        Generate test user and set password.
        """
        user = TimeTrackUserFactory.build(**kwargs)
        user.set_password(password)
        user.save()
        return user
