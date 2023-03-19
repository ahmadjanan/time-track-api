from django.contrib import admin
from django.urls import include, path

from api import urls as api_urls


urlpatterns = [
    # path("admin/doc/", include("django.contrib.admindocs.urls")),
    # path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
]
