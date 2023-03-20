from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response

from api.projects.models import Project
from api.projects.permissions.project_permissions import ProjectPermissions
from api.projects.serializers.project_serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Project ViewSet
    """
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, ProjectPermissions, )
    queryset = Project.objects.all().select_related("owner")

    def perform_create(self, serializer: ProjectSerializer) -> None:
        """
        Sets project owner to request.user
        """
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs) -> Response:
        """
        Override default response of the destroy method.
        """
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
