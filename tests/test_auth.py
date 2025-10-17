from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': 'senha'}
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_invalid_email(client, user):
    response = client.post(
        '/auth/token/', data={'username': '', 'password': 'senha'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_invalid_password(client, user):
    response = client.post(
        '/auth/token/', data={'username': user.email, 'password': ''}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}
