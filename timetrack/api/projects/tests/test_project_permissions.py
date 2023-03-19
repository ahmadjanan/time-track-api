import pytest

from api.projects.tests.factories import ProjectFactory
from api.users.tests.factories import TimeTrackUserFactory


@pytest.mark.django_db
def test_project_safe_methods(client):
    """
    Test project safe method
    """
    first_user = TimeTrackUserFactory.with_password(password="secret123")
    second_user = TimeTrackUserFactory.with_password(
        email="user2@test.com",
        username="user2",
        password="secret123",
    )
    project = ProjectFactory.with_owner(owner=first_user)

    client.force_authenticate(user=second_user)
    resp = client.get(f"/api/projects/{project.uuid}")
    assert resp.status_code == 200

    client.force_authenticate(user=first_user)
    resp = client.get(f"/api/projects/{project.uuid}")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_project_unsafe_methods(client):
    """
    Test project unsafe methods
    """
    first_user = TimeTrackUserFactory.with_password(password="secret123")
    second_user = TimeTrackUserFactory.with_password(
        email="user2@test.com",
        username="user2",
        password="secret123",
    )
    project = ProjectFactory.with_owner(owner=first_user)

    client.force_authenticate(user=second_user)
    resp = client.delete(f"/api/projects/{project.uuid}")
    assert resp.status_code == 403
    resp = client.patch(f"/api/projects/{project.uuid}")
    assert resp.status_code == 403
    resp = client.put(
        f"/api/projects/{project.uuid}",
        data={
            "name": "Updated project name",
            "description": "Updated project description",
        }
    )
    assert resp.status_code == 403

    client.force_authenticate(user=first_user)
    resp = client.patch(f"/api/projects/{project.uuid}")
    assert resp.status_code == 200
    resp = client.put(
        f"/api/projects/{project.uuid}",
        data={
            "name": "Updated project name",
            "description": "Updated project description",
        }
    )
    assert resp.status_code == 200
    resp = client.delete(f"/api/projects/{project.uuid}")
    assert resp.status_code == 204
