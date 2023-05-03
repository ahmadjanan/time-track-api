from rest_framework import permissions

from api.projects.permissions.utils import is_superuser


class ProjectPermissions(permissions.BasePermission):
    """
    Project Permissions setup
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user has the object permission.
        Allows safe requests to everyone, and checks object ownership/superuser status for unsafe requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return is_superuser(request.user) or request.user == obj.owner
