from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from api.projects.models import TimeLog, Project, ProjectMember
from api.projects.permissions.log_permissions import TimeLogPermissions
from api.projects.serializers.log_serializer import TimeLogSerializer


class TimeLogListCreateView(generics.ListCreateAPIView):
    """
    List all time logs or create a new time log
    """
    serializer_class = TimeLogSerializer
    permission_classes = (IsAuthenticated, TimeLogPermissions, )
    queryset = TimeLog.objects.all()

    def get_queryset(self):
        """
        If Project uuid is found in request kwargs, limits Logs' queryset to the project's Logs.
        If Project uuid is not found, limits Logs' queryset to Projects joined by request.user.
        """
        projects_uuids = self.request.user.projects.values_list("project__uuid", flat=True)
        queryset = super().get_queryset().filter(member__project__uuid__in=projects_uuids)
        if self.kwargs.get("uuid"):
            project = get_object_or_404(Project, uuid=self.kwargs["uuid"])
            return queryset.filter(member__project=project)

        return queryset.filter(member__user=self.request.user)

    def perform_create(self, serializer):
        """
        Fetch ProjectMember instance using project uuid and request.user and set the Log's Member FK.
        """
        project_uuid = self.kwargs.get("uuid") or self.request.data.get("project_uuid")
        if not project_uuid:
            raise ValidationError({"message": "project_uuid not found."})

        member = ProjectMember.objects.get(project__uuid=project_uuid, user=self.request.user)
        serializer.save(member=member)


class TimeLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a time log instance.
    """
    serializer_class = TimeLogSerializer
    permission_classes = (IsAuthenticated, TimeLogPermissions, )
    lookup_field = "uuid"

    def get_queryset(self):
        """
        Limit queryset to Logs belonging to Projects joined by request.user
        """
        projects_uuids = self.request.user.projects.values_list("project__uuid", flat=True)
        return TimeLog.objects.filter(member__project__uuid__in=projects_uuids)
