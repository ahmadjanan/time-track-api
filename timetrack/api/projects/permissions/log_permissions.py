from rest_framework import permissions

from api.projects.permissions.utils import is_superuser


class TimeLogPermissions(permissions.BasePermission):
    """
    Time Log Permissions setup
    """
    @staticmethod
    def is_owner(user, obj):
        return user == obj.member.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.uuid in obj.member.project.members.values_list("user__uuid", flat=True)

        return is_superuser(request.user) or self.is_owner(request.user, obj)
