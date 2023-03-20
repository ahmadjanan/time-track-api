from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from api.users.views.change_password import ChangePasswordView
from api.users.views.create_view import TimeTrackUserCreateView
from api.users.views.retrieve_update_view import TimeTrackUserRetrieveUpdateView

urlpatterns = [
    path('register', TimeTrackUserCreateView.as_view(), name='create-user'),
    path('profile', TimeTrackUserRetrieveUpdateView.as_view(), name='retrieve-update-profile'),
    path('login', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token-verify'),
    path('change_password', ChangePasswordView.as_view(), name='password-change'),
    path('<uuid:uuid>', TimeTrackUserRetrieveUpdateView.as_view(), name='retrieve-user'),
]
