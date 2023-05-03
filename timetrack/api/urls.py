from django.urls import path, include

from api.projects import urls as projects_urls
from api.users import urls as users_urls

urlpatterns = [
    path(r'projects/', include(projects_urls)),
    path(r'users/', include(users_urls)),
]
