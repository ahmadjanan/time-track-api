import pytest
from rest_framework.test import APIClient

from api.projects.tests.factories import ProjectFactory
from api.users.tests.factories import TimeTrackUserFactory


@pytest.mark.django_db
def test_project_create(client: APIClient) -> None:
    """
    Test project create
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    resp = client.post(
        "/api/projects/",
        data={"description": "Test Description", "name": "Test Project"},
    )

    assert resp.status_code == 201


@pytest.mark.django_db
def test_project_retrieve(client: APIClient) -> None:
    """
    Test project retrieve
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    project = ProjectFactory.with_owner(owner=user)
    resp = client.get(f"/api/projects/{project.uuid}")

    assert resp.status_code == 200

    resp = resp.json()
    assert resp.get("uuid") == str(project.uuid)
    assert resp.get("owner", {}).get("uuid") == str(project.owner.uuid)
    assert resp.get("name") == project.name
    assert resp.get("description") == project.description


@pytest.mark.django_db
def test_project_delete(client: APIClient) -> None:
    """
    Test project delete
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    project = ProjectFactory.with_owner(owner=user)
    resp = client.delete(f"/api/projects/{project.uuid}")

    assert resp.status_code == 204


@pytest.mark.django_db
def test_project_update(client: APIClient) -> None:
    """
    Test project update
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    project = ProjectFactory.with_owner(owner=user)
    patch_data = {
        "name": "Updated Project Name",
        "description": "Updated Project Description",
    }
    resp = client.patch(f"/api/projects/{project.uuid}", data=patch_data)

    assert resp.status_code == 200

    resp = resp.json()
    assert resp.get("name") == patch_data["name"]
    assert resp.get("description") == patch_data["description"]
