from rest_framework import serializers

from api.projects.models import ProjectMember
from api.users.serializers.user_retrieve_update_serializer import UserSerializer


class ProjectMemberSerializer(serializers.ModelSerializer):
    """
    Serializer for ProjectMember CRUD views.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = ("uuid", "user", )
        read_only_fields = ("uuid", "user", )
