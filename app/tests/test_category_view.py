from fastapi.testclient import TestClient


def test_category_create(client: TestClient, admin_auth_header):
    response = client.post('/categories/',
                           headers=admin_auth_header,
                           json={'name': 'Categoria 1'})
    assert response.status_code == 201

    assert response.json()['id'] == 1  # get id in categories
    """ response = client.get('/categories/1')
    assert response.json()['name'] == 'Categoria 1' """


def test_category_update(client: TestClient, admin_auth_header):
    response = client.post('/categories/',
                           headers=admin_auth_header,
                           json={'name': 'Categoria 1'})
    assert response.status_code == 201

    response = client.put('/categories/1',
                          headers=admin_auth_header,
                          json={'name': 'Categoria alterada'})
    assert response.status_code == 200

    response = client.get('/categories/1', headers=admin_auth_header)
    assert response.json()['name'] == 'Categoria alterada'
