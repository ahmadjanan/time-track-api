from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from api.users.serializers.user_create_serializer import UserCreateSerializer

USER_MODEL = get_user_model()


class TimeTrackUserCreateView(CreateAPIView):
    """
    User Register View
    """
    queryset = USER_MODEL.objects.all()
    serializer_class = UserCreateSerializer
    authentication_classes = ()
    permission_classes = ()
