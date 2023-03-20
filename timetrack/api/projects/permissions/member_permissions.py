from rest_framework import permissions

from api.projects.permissions.utils import is_superuser, is_approved_project_member


class ProjectMemberPermissions(permissions.BasePermission):
    """
    Project Member Permissions setup
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user has the object permission.
        Allows safe requests to same project's approved members, and checks ownership/superuser status for
        unsafe requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return is_approved_project_member(request.user, obj.project)

        return is_superuser(request.user) or request.user == obj.project.owner or request.user == obj.user
