from http import HTTPStatus


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


def test_get_all_users(client):
    response = client.get('/users/')
    response_data = response.json()

    for user in response_data.get('users'):
        assert 'created_at' in user
        assert 'id' in user

        user.pop('created_at')
        user.pop('id')

    assert response.status_code == HTTPStatus.OK
    assert response_data == {
        'users': [
            {
                'name': 'lucas',
                'phone_number': '61991052451',
                'email': 'lucassaadro@gmail.com',
            }
        ]
    }


def test_put_user_by_id(client):
    response = client.put(
        '/users/0',
        json={
            'name': 'saad',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha'
        }
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


def test_put_user_by_id_fail(client):
    response = client.put(
        '/users/999',
        json={
            'name': 'saad',
            'phone_number': '61991052451',
            'email': 'lucassaadro@gmail.com',
            'password': 'senha'
        }
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_by_id(client):
    response = client.delete(
        '/users/0'
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted'
    }


def test_delete_user_by_id_fail(client):
    response = client.delete(
    '/users/999'
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
