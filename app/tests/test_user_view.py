from fastapi.testclient import TestClient


def test_user_create(client: TestClient, admin_auth_header, user_factory):
    user_admin = user_factory

    response = client.post('/users_admin/',
                           headers=admin_auth_header,
                           json={
                               'display_name': 'teste',
                               'email': 'teste@email.com',
                               'role': 'admin',
                               'password': user_admin.password
                           })
    assert response.status_code == 200
    id = response.json()['id']

    response = client.get(f'/users_admin/{id}',
                          headers=admin_auth_header)
    assert response.json()['email'] == 'teste@email.com'


def test_user_create_with_same_email(client: TestClient, admin_auth_header, user_factory):
    user_admin = user_factory

    response = client.post('/users_admin/',
                           headers=admin_auth_header,
                           json={
                               'display_name': 'teste123',
                               'email': 'teste@email.com',
                               'role': 'admin',
                               'password': user_admin.password
                           })
    assert response.status_code == 200

    response = client.post('/users_admin/',
                        headers=admin_auth_header,
                        json={
                            'display_name': 'teste123',
                            'email': 'teste@email.com',
                            'role': 'admin',
                            'password': user_admin.password
                        })
    assert response.status_code == 400


def test_user_update(client: TestClient, admin_auth_header, user_factory):
    user_admin = user_factory

    response = client.post('/users_admin/',
                           headers=admin_auth_header,
                           json={
                               'display_name': 'teste',
                               'email': 'teste@email.com',
                               'role': 'admin',
                               'password': user_admin.password
                           })
    assert response.status_code == 200
    id = response.json()['id']

    response = client.put(f'/users_admin/{id}',
                          headers=admin_auth_header,
                          json={
                              'display_name': 'teste',
                              'email': 'teste123@email.com',
                              'role': 'admin',
                              'password': user_admin.password
                          })
    assert response.status_code == 200

    response = client.get(
        f'/users_admin/{id}', headers=admin_auth_header)
    assert response.json()['email'] == 'teste123@email.com'


def test_user_delete(client: TestClient, admin_auth_header, user_factory):
    user_admin = user_factory
    response = client.post('/users_admin/',
                           headers=admin_auth_header,
                           json={
                               'display_name': 'teste',
                               'email': 'teste@email.com',
                               'role': 'admin',
                               'password': user_admin.password
                           })
    assert response.status_code == 200
    id = response.json()['id']

    response = client.get(
        f'/users_admin/{id}', headers=admin_auth_header)
    assert response.json()['email'] == 'teste@email.com'
    
    response = client.delete(f'/users_admin/{id}',
                             headers=admin_auth_header,
                             json={'id': 'pyint'})
    assert response.status_code == 202
