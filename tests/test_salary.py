from conftest import client


def test_get_user_salary_nonauthorized():
    response = client.get('/user/salary')

    assert response.status_code == 401


def test_get_user_salary_autahorized():
    response = client.post('/auth/register', json={
        'email': 'test10@example.com',
        'password': 'string',
        'is_active': True,
        'is_superuser': False,
        'is_verified': False,
        'salary': 0,
        'date_on_next_increase': '2023-06-19'
    })

    response = client.post('/auth/jwt/login', data={
        'username': 'test10@example.com',
        'password': 'string'
    })
    response = client.get('/user/salary', cookies=dict(response.cookies))

    assert response.status_code == 200
