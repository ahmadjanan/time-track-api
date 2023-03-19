from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.projects.models import ProjectMember, Project
from api.projects.permissions.member_permissions import ProjectMemberPermissions
from api.projects.serializers.member_serializer import ProjectMemberSerializer


class ProjectMemberListCreateView(generics.ListCreateAPIView):
    """
    View to list all project members or create a new project member
    """
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = (IsAuthenticated, ProjectMemberPermissions, )

    def get_queryset(self):
        """
        If Project uuid is found in request kwargs, limits Members' queryset to the project's Logs.
        If Project uuid is not found, limits Members' queryset to Projects joined by request.user.
        """
        projects_uuids = self.request.user.projects.values_list("project__uuid", flat=True)
        queryset = super().get_queryset().filter(project__uuid__in=projects_uuids)
        if self.kwargs.get("uuid"):
            project = get_object_or_404(Project, uuid=self.kwargs["uuid"])
            return queryset.filter(project=project)

        return queryset

    def perform_create(self, serializer):
        project = get_object_or_404(Project, uuid=self.kwargs["uuid"])
        serializer.save(project=project, user=self.request.user)


class ProjectMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a project member
    """
    serializer_class = ProjectMemberSerializer
    permission_classes = (IsAuthenticated, ProjectMemberPermissions, )
    lookup_field = "uuid"

    def get_queryset(self):
        """
        Limit queryset to Members belonging to Projects joined by request.user
        """
        projects_uuids = self.request.user.projects.values_list("project__uuid", flat=True)
        return ProjectMember.objects.filter(project__uuid__in=projects_uuids)
