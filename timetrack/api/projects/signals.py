from django.db.models.signals import post_save
from django.dispatch import receiver

from api.projects.models import Project, ProjectMember


@receiver(post_save, sender=Project)
def make_owner_project_member(instance, created, **kwargs):
    """
    Signal to make the project creator a member of the project.
    """
    if created:
        ProjectMember.objects.create(user=instance.owner, project=instance)
