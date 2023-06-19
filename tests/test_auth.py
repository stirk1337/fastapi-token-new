from test import client


def test_register():
    response = client.post("/auth/register", json={
        "email": "test7@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "salary": 0,
        "date_on_next_increase": "2023-06-19"
    })

    assert response.status_code == 201


def test_login():
    response = client.post("/auth/register", json={
        "email": "test10@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "salary": 0,
        "date_on_next_increase": "2023-06-19"
    })

    response = client.post("/auth/jwt/login", data={
        "username": "test10@example.com",
        "password": "string"
    })

    assert response.status_code == 204


def test_logout():
    response = client.post("/auth/jwt/logout")

    assert response.status_code == 401

    response = client.post("/auth/register", json={
        "email": "test10@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "salary": 0,
        "date_on_next_increase": "2023-06-19"
    })

    response = client.post("/auth/jwt/login", data={
        "username": "test10@example.com",
        "password": "string"
    })
    response = client.post("/auth/jwt/logout", cookies=dict(response.cookies))

    assert response.status_code == 204
