from rest_framework import routers

from api.projects.views.application_viewset import ApplicationViewSet
from api.projects.views.log_viewset import TimeLogViewSet
from api.projects.views.member_viewset import ProjectMemberViewSet
from api.projects.views.project_viewset import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewSet, basename='projects')
router.register(r'applications', ApplicationViewSet, basename='all-applications')
router.register(r'members', ProjectMemberViewSet, basename='all-members')
router.register(r'logs', TimeLogViewSet, basename='all-members')
router.register(r'(?P<project_uuid>[^/.]+)/applications', ApplicationViewSet, basename='project-applications')
router.register(r'(?P<project_uuid>[^/.]+)/members', ProjectMemberViewSet, basename='project-members')
router.register(r'(?P<project_uuid>[^/.]+)/logs', TimeLogViewSet, basename='project-logs')
router.register(r'members/(?P<member_uuid>[^/.]+)/logs', TimeLogViewSet, basename='member-logs')

urlpatterns = router.urls
