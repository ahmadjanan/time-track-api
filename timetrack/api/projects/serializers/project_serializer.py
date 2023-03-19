from rest_framework import serializers

from api.projects.models import Project
from api.users.serializers.user_retrieve_update_serializer import UserRetrieveUpdateSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ("uuid", "name", "description", "owner", )
        read_only_fields = ("owner", "uuid", )
