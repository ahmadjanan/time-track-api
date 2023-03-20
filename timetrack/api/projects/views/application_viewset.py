from django.db.models import QuerySet, Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.projects.models import ProjectMember, Project
from api.projects.permissions.application_permissions import ApplicationPermissions
from api.projects.serializers.application_serializer import ApplicationSerializer


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
            Q(status=ProjectMember.Status.PENDING)
        )

        if self.kwargs.get("uuid"):
            project = get_object_or_404(Project, uuid=self.kwargs["uuid"])
            return queryset.filter(project=project)

        return queryset

    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Override default response of the destroy method.
        """
        super().destroy(request, *args, **kwargs)
        return Response({"message": "application deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
