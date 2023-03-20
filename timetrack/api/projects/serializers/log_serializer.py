from rest_framework import serializers

from api.projects.models import TimeLog
from api.projects.serializers.member_serializer import ProjectMemberSerializer


class TimeLogSerializer(serializers.ModelSerializer):
    """
    Serializer for TimeLog CRUD views.
    """
    member = ProjectMemberSerializer(read_only=True)

    class Meta:
        model = TimeLog
        fields = ("uuid", "start_time", "end_time", "member", "description", )
