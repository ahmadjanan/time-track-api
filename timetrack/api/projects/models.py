import uuid

from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class Project(models.Model):
    """
    A project model for tracking work time
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(USER_MODEL, related_name="owned_project", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    """
    A model for keeping track of project members
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    project = models.ForeignKey(Project, related_name="members", on_delete=models.CASCADE)
    user = models.ForeignKey(USER_MODEL, related_name="projects", on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("project", "user", )

    def __str__(self):
        return f"{self.project.name} - {self.user.get_full_name()}"


class TimeLog(models.Model):
    """
    A model for logging work time
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=255)
    member = models.ForeignKey(ProjectMember, related_name="logs", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.project.name} - {self.member.user.get_full_name()}: {self.start_time} to {self.end_time}"
