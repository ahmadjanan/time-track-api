from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for user RUD views.
    """
    class Meta:
        model = USER_MODEL
        fields = ('uuid', 'email', 'first_name', 'last_name', )
        read_only_fields = ('uuid', )


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for short user info.
    """
    name = serializers.SerializerMethodField()

    class Meta:
        model = USER_MODEL
        fields = ('uuid', 'name', )

    def get_name(self, instance: USER_MODEL) -> str:
        """
        Get the full name of a user.
        """
        return instance.get_full_name()
