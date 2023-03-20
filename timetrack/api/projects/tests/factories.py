from django.conf import settings
from factory.django import DjangoModelFactory

from api.projects.models import Project


class ProjectFactory(DjangoModelFactory):
    """
    Project Factory for generating test Project instances in database.
    """
    class Meta:
        model = Project
        django_get_or_create = ("uuid", )

    name = "Test Project"
    description = "Test Project Description"

    @staticmethod
    def with_owner(owner: settings.AUTH_USER_MODEL, **kwargs) -> Project:
        """
        Generate test project and set owner.
        """
        project = ProjectFactory.build(owner=owner, **kwargs)
        project.save()
        return project
