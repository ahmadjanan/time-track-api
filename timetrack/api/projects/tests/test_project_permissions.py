import pytest
from rest_framework.test import APIClient

from api.projects.models import Project
from api.projects.tests.factories import ProjectFactory
from api.users.tests.factories import TimeTrackUserFactory


@pytest.fixture
def project() -> Project:
    """
    Pytest fixture to generate a user with a project
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    project = ProjectFactory.with_owner(owner=user)

    return project


@pytest.mark.django_db
def test_project_owner_safe_method(client: APIClient, project: Project) -> None:
    """
    Test project owner safe method
    """
    client.force_authenticate(user=project.owner)
    resp = client.get(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_project_non_owner_safe_method(client: APIClient, project: Project) -> None:
    """
    Test project non-owner safe method
    """
    user = TimeTrackUserFactory.with_password(
        email="user2@test.com",
        username="user2",
        password="secret123",
    )

    client.force_authenticate(user=user)
    resp = client.get(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_project_owner_unsafe_methods(client: APIClient, project: Project) -> None:
    """
    Test project owner unsafe methods
    """
    client.force_authenticate(user=project.owner)
    resp = client.patch(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 200
    resp = client.put(
        f"/api/projects/{project.uuid}/",
        data={
            "name": "Updated project name",
            "description": "Updated project description",
        }
    )
    assert resp.status_code == 200
    resp = client.delete(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 204


@pytest.mark.django_db
def test_project_non_owner_unsafe_methods(client: APIClient, project: Project) -> None:
    """
    Test project non-owner unsafe methods
    """
    user = TimeTrackUserFactory.with_password(
        email="user2@test.com",
        username="user2",
        password="secret123",
    )

    client.force_authenticate(user=user)
    resp = client.delete(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 403
    resp = client.patch(f"/api/projects/{project.uuid}/")
    assert resp.status_code == 403
    resp = client.put(
        f"/api/projects/{project.uuid}/",
        data={
            "name": "Updated project name",
            "description": "Updated project description",
        }
    )
    assert resp.status_code == 403
