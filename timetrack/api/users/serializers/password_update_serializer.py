from typing import Dict, Any

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import serializers

USER_MODEL = get_user_model()


class PasswordUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = USER_MODEL
        fields = ('old_password', 'new_password')

    def validate_old_password(self, value: str) -> str:
        """
        Validate the old password of the user with the DB.
        """
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError('Incorrect password.')
        return value

    def update(self, instance, validated_data: Dict[str, Any]):
        """
        Update the user's password in the DB.
        """
        user = self.context['request'].user
        user.set_password(validated_data['new_password'])
        user.save()
        return user
