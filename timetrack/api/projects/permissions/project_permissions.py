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
        return user == obj.owner

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return is_superuser(request.user) or self.is_owner(request.user, obj)
