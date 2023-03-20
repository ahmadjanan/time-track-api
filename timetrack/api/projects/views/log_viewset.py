from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.projects.models import TimeLog, Project, ProjectMember
from api.projects.permissions.log_permissions import TimeLogPermissions
from api.projects.serializers.log_serializer import TimeLogSerializer


class TimeLogViewSet(viewsets.ModelViewSet):
    """
    Time Log ViewSet
    """
    serializer_class = TimeLogSerializer
    permission_classes = (IsAuthenticated, TimeLogPermissions, )

    def get_queryset(self) -> QuerySet:
        """
        If Project uuid is found in request kwargs, limits Logs' queryset to the project.
        If Project uuid is not found, limits Logs' queryset to Projects joined by request.user.
        """
        projects_uuids = self.request.user.project_memberships.values_list("project__uuid", flat=True)
        queryset = TimeLog.objects.filter(
            member__project__uuid__in=projects_uuids,
            member__status=ProjectMember.Status.APPROVED
        )
        if self.kwargs.get("project_uuid"):
            project = get_object_or_404(Project, uuid=self.kwargs["project_uuid"])
            return queryset.filter(member__project=project)

        return queryset

    def perform_create(self, serializer: TimeLogSerializer) -> None:
        """
        Fetch ProjectMember instance using project uuid and request.user and set the Log's Member FK.
        """
        project_uuid = self.kwargs.get("project_uuid") or self.request.data.get("project_uuid")
        if not project_uuid:
            raise ValidationError({"message": "project_uuid not found."})

        member = get_object_or_404(ProjectMember, project__uuid=project_uuid, user=self.request.user)
        serializer.save(member=member)

    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Override default response of the destroy method.
        """
        super().destroy(request, *args, **kwargs)
        return Response({"message": "log deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
