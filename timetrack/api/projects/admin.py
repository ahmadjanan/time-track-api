from django.contrib import admin

from api.projects.models import Project, ProjectMember, TimeLog

admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(TimeLog)
