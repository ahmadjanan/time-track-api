from django.conf import settings
from rest_framework import permissions

from api.projects.models import Project
from api.projects.permissions.utils import is_superuser


class ProjectPermissions(permissions.BasePermission):
    """
    Project Permissions setup
    """
    @staticmethod
    def is_owner(user: settings.AUTH_USER_MODEL, obj: Project) -> bool:
        """
        Checks whether the requesting user is the owner of the Project object.
        """
        return user == obj.owner

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user has the object permission.
        Allows safe requests to everyone, and checks object ownership/superuser status for unsafe requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return is_superuser(request.user) or self.is_owner(request.user, obj)
