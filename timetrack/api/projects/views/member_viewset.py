from django.db import IntegrityError
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.projects.models import ProjectMember, Project
from api.projects.permissions.member_permissions import ProjectMemberPermissions
from api.projects.serializers.member_serializer import ProjectMemberSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    """
    Project Member ViewSet
    """
    serializer_class = ProjectMemberSerializer
    permission_classes = (IsAuthenticated, ProjectMemberPermissions, )

    def get_queryset(self) -> QuerySet:
        """
        If Project uuid is found in request kwargs, limits Members' queryset to the project.
        If Project uuid is not found, limits Members' queryset to Projects joined by request.user.
        """
        projects_uuids = self.request.user.project_memberships.filter(
            status=ProjectMember.Status.APPROVED
        ).values_list("project__uuid", flat=True)

        queryset = ProjectMember.objects.filter(
            project__uuid__in=projects_uuids,
            status=ProjectMember.Status.APPROVED
        )

        if self.kwargs.get("project_uuid"):
            project = get_object_or_404(Project, uuid=self.kwargs["project_uuid"])
            return queryset.filter(project=project)

        return queryset

    def perform_create(self, serializer: ProjectMemberSerializer) -> None:
        """
        Fetch Project instance using project uuid and request.user and set the ProjectMember's Project FK.
        """
        project = get_object_or_404(Project, uuid=self.kwargs["project_uuid"])
        try:
            serializer.save(project=project, user=self.request.user)
        except IntegrityError:
            raise ValidationError({"message": "already applied to this project."})

    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Override default response of the destroy method.
        """
        super().destroy(request, *args, **kwargs)
        return Response({"message": "member removed successfully."}, status=status.HTTP_204_NO_CONTENT)
