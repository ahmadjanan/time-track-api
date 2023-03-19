from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.projects'

    def ready(self):
        from api.projects.signals import make_owner_project_member
