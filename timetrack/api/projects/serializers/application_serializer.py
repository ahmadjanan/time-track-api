from rest_framework import serializers

from api.projects.models import ProjectMember
from api.users.serializers.user_retrieve_update_serializer import UserSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for Application ViewSet.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProjectMember
        fields = ("uuid", "user", "status", )
        read_only_fields = ("uuid", "user", )
