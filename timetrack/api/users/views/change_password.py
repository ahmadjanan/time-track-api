from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.users.serializers.password_update_serializer import PasswordUpdateSerializer

USER_MODEL = get_user_model()


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = PasswordUpdateSerializer
    queryset = USER_MODEL.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        """
        Update a user's password and raise errors, if any.
        """
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "password updated successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
