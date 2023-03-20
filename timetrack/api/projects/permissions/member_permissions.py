from django.conf import settings
from rest_framework import permissions

from api.projects.models import ProjectMember
from api.projects.permissions.utils import is_superuser


class ProjectMemberPermissions(permissions.BasePermission):
    """
    Project Member Permissions setup
    """
    @staticmethod
    def is_owner(user: settings.AUTH_USER_MODEL, obj: ProjectMember) -> bool:
        """
        Checks whether the requesting user is the user of the ProjectMember object.
        """
        return user == obj.user

    @staticmethod
    def is_project_owner(user: settings.AUTH_USER_MODEL, obj: ProjectMember) -> bool:
        """
        Checks whether the requesting user is the owner of the Project of the ProjectMember object.
        """
        return user == obj.project.owner

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user has the object permission.
        Allows safe requests to same project members, and checks ownership/superuser status for unsafe requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return request.user.uuid in obj.project.members.values_list("user__uuid", flat=True)

        return is_superuser(request.user) or self.is_project_owner(request.user, obj) or self.is_owner(request.user, obj)
