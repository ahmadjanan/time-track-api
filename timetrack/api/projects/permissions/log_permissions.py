from django.conf import settings
from rest_framework import permissions

from api.projects.models import TimeLog
from api.projects.permissions.utils import is_superuser


class TimeLogPermissions(permissions.BasePermission):
    """
    Time Log Permissions setup
    """
    @staticmethod
    def is_owner(user: settings.AUTH_USER_MODEL, obj: TimeLog) -> bool:
        """
        Checks whether the requesting user is the owner of the TimeLog object.
        """
        return user == obj.member.user

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks whether the requesting user has the object permission.
        Allows safe requests to same project members, and checks object ownership/superuser status for unsafe requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return request.user.uuid in obj.member.project.members.values_list("user__uuid", flat=True)

        return is_superuser(request.user) or self.is_owner(request.user, obj)
