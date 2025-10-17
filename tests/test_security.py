from http import HTTPStatus

from jwt import decode

from tradefair_system.security import create_access_token, settings


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded_jwt = decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    assert decoded_jwt['test'] == data['test']
    assert 'exp' in decoded_jwt


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
