from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.projects.models import Project
from api.projects.permissions.project_permissions import ProjectPermissions
from api.projects.serializers.project_serializer import ProjectSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    """
    Endpoint for listing and creating projects.
    """
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, ProjectPermissions, )
    queryset = Project.objects.all()

    def perform_create(self, serializer: ProjectSerializer) -> None:
        """
        Sets project owner to request.user
        """
        serializer.save(owner=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for retrieving, updating and deleting a project.
    """
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, ProjectPermissions, )
    queryset = Project.objects.all()
    lookup_field = "uuid"

    def delete(self, request, *args, **kwargs) -> Response:
        super().delete(request, *args, **kwargs)
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
