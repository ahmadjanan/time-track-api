import pytest

from api.users.tests.factories import TimeTrackUserFactory


@pytest.mark.django_db
def test_profile_retrieve(client):
    """
    Test user profile retrieve
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    resp = client.get("/api/users/profile")
    assert resp.status_code == 200

    resp = resp.json()
    assert resp.get("uuid") == str(user.uuid)
    assert resp.get("email") == user.email
    assert resp.get("first_name") == user.first_name
    assert resp.get("last_name") == user.last_name


@pytest.mark.django_db
def test_profile_update(client):
    """
    Test user profile update
    """
    user = TimeTrackUserFactory.with_password(password="secret123")
    client.force_authenticate(user=user)
    data = {
        "email": "updated@test.com",
        "first_name": "Updated First Name",
        "last_name": "Updated Last Name",
    }
    resp = client.patch("/api/users/profile", data=data)
    assert resp.status_code == 200

    resp = resp.json()
    assert resp.get("uuid") == str(user.uuid)
    assert resp.get("email") == data["email"]
    assert resp.get("first_name") == data["first_name"]
    assert resp.get("last_name") == data["last_name"]
