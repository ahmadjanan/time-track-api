from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from api.users.serializers.user_retrieve_update_serializer import UserRetrieveUpdateSerializer

USER_MODEL = get_user_model()


class TimeTrackUserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserRetrieveUpdateSerializer
    lookup_field = 'uuid'
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        """
        Returns the requesting user's profile if no UUID is found in URL kwargs
        """
        if not self.kwargs.get('uuid'):
            return USER_MODEL.objects.get(uuid=self.request.user.uuid)
        return super().get_object()
