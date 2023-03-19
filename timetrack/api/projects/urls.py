from django.urls import path

from api.projects.views.log_crud import TimeLogListCreateView, TimeLogDetailView
from api.projects.views.member_crud import ProjectMemberListCreateView, ProjectMemberDetailView
from api.projects.views.project_crud import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    # Project views
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
    path('<uuid:uuid>', ProjectDetailView.as_view(), name='project-rud'),
    path('<uuid:uuid>/members', ProjectMemberListCreateView.as_view(), name='project-members-list'),
    path('<uuid:uuid>/logs', TimeLogListCreateView.as_view(), name='project-logs-list'),

    # ProjectMember views
    path('members/<uuid:uuid>', ProjectMemberDetailView.as_view(), name='member-rud'),

    # TimeLog views
    path('logs', TimeLogListCreateView.as_view(), name='logs-self-list'),
    path('logs/<uuid:uuid>', TimeLogDetailView.as_view(), name='log-rud'),
]
