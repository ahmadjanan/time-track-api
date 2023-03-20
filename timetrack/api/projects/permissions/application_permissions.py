from rest_framework import permissions

from api.projects.permissions.utils import is_superuser


class ApplicationPermissions(permissions.BasePermission):
    """
    Application Permissions setup
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user is the Project owner or Application owner.
        Only allows Application owner and Superuser to delete the Application.
        """
        if view.action == 'destroy':
            return is_superuser(request.user) or request.user == obj.user

        return request.user == obj.project.owner or request.user == obj.user
