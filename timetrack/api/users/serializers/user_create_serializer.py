from typing import Dict, Any

from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = USER_MODEL
        fields = ('uuid', 'email', 'username', 'password', 'first_name', 'last_name', 'date_joined', 'is_active', )
        read_only_fields = ('uuid', )

    def create(self, validated_data: Dict[str, Any]):
        return USER_MODEL.objects.create_user(**validated_data)
