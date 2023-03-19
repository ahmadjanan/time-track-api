from rest_framework import permissions

from api.projects.permissions.utils import is_superuser


class ProjectMemberPermissions(permissions.BasePermission):
    """
    Project Member Permissions setup
    """
    @staticmethod
    def is_owner(user, obj):
        return user == obj.user

    @staticmethod
    def is_project_owner(user, obj):
        return user == obj.project.owner

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.uuid in obj.project.members.values_list("user__uuid", flat=True)

        return is_superuser(request.user) or self.is_project_owner(request.user, obj) or self.is_owner(request.user, obj)
