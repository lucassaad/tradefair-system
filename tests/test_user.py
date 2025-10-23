from http import HTTPStatus

import pytest

from tradefair_system.schemas.user import UserOut


@pytest.mark.asyncio
def test_post_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'lucas',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha',
        },
    )

    response_data = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert 'created_at' in response_data
    assert 'id' in response_data

    response_data.pop('created_at')
    response_data.pop('id')

    assert response_data == {
        'name': 'lucas',
        'phone_number': '61991052451',
        'email': 'lucassaadro@gmail.com',
    }


def test_post_user_already_exists(client):
    client.post(
        '/users/',
        json={
            'name': 'lucas',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha',
        },
    )

    response = client.post(
        '/users/',
        json={
            'name': 'Saad',
            'phone_number': '61982785801',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_get_all_users_without_user(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_get_all_users_with_users(client, user):
    user_schema = UserOut.model_validate(user).model_dump()
    user_schema['created_at'] = user_schema['created_at'].isoformat()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_put_user_by_id(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'saad',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha_teste',
        },
    )
    response_data = response.json()

    assert response.status_code == HTTPStatus.OK

    response_data.pop('id')
    response_data.pop('created_at')

    assert response_data == {
        'name': 'saad',
        'phone_number': '61991052451',
        'email': 'lucassaadro@gmail.com',
    }


def test_put_user_by_id_fail(client, user, token):
    response = client.put(
        '/users/999',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'saad',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN


def test_put_integrity_error(client, user, token):
    client.post(
        '/users/',
        json={
            'name': 'lucas',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha',
        },
    )
    response_update = client.put(
        f'/users/{user.id}/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'teste',
            'phone_number': '00000000000',
            'email': 'lucassaadro@gmail.com',
            'password': 'psswd',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {'detail': 'Email already exists'}


def test_delete_user_by_id(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_by_id_fail(client, user, token):
    response = client.delete(
        '/users/999', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
