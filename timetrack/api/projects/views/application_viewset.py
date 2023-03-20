from django.db import IntegrityError
from django.db.models import QuerySet, Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.projects.models import ProjectMember, Project
from api.projects.permissions.application_permissions import ApplicationPermissions
from api.projects.serializers.application_serializer import ApplicationSerializer
from api.projects.serializers.member_serializer import ProjectMemberSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    Project Application ViewSet
    """
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated, ApplicationPermissions, )

    def get_queryset(self) -> QuerySet:
        """
        If Project uuid is found in request kwargs, limits Applications' queryset to the project.
        If Project uuid is not found, limits Applications' queryset to Projects owned by request.user.
        """
        queryset = ProjectMember.objects.filter(
            (Q(project__owner=self.request.user) | Q(user=self.request.user)) &
            ~Q(status=ProjectMember.Status.APPROVED)
        )

        if self.kwargs.get("uuid"):
            return queryset.filter(project__uuid=self.kwargs["uuid"])

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
        return Response({"message": "application deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
