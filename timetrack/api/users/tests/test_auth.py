import pytest

from api.users.tests.factories import TimeTrackUserFactory


@pytest.mark.django_db
def test_login(client):
    """
    Test user login
    """
    user = TimeTrackUserFactory.with_password(password="secret123")

    resp = client.post(
        "/api/users/login",
        data={"email": user.email, "password": "secret123"},
    )

    assert resp.status_code == 200

    resp = resp.json()
    assert "access" in resp.keys()
    assert "refresh" in resp.keys()


@pytest.mark.django_db
def test_register(client):
    """
    Test user register
    """
    resp = client.post(
        "/api/users/register",
        data={
            "email": "test@example.com",
            "username": "test",
            "first_name": "Test",
            "last_name": "User",
            "password": "S3cr3t?N0tR34lly",
        },
    )

    assert resp.status_code == 201

    resp = resp.json()
    assert "uuid" in resp.keys()
    assert "email" in resp.keys()
    assert "username" in resp.keys()
    assert "first_name" in resp.keys()
    assert "last_name" in resp.keys()
    assert "date_joined" in resp.keys()
