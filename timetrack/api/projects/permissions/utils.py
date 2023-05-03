from django.conf import settings

from api.projects.models import Project, ProjectMember


def is_superuser(user: settings.AUTH_USER_MODEL) -> bool:
    """
    Checks whether a user is a superuser.
    """
    return user.is_authenticated and user.is_superuser


def is_approved_project_member(user: settings.AUTH_USER_MODEL, project: Project) -> bool:
    """
    Checks whether a user is an approved project member.
    """
    return user.uuid in project.project_memberships.filter(
        status=ProjectMember.Status.APPROVED
    ).values_list("user__uuid", flat=True)
