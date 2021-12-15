from fastapi.testclient import TestClient


def test_supplier_create(client: TestClient, admin_auth_header):
    response = client.post('/suppliers/',
                           headers=admin_auth_header,
                           json={'name': 'LG'})
    assert response.status_code == 201
    
    assert response.json()['id'] == 1


def test_supplier_update(client: TestClient, admin_auth_header):
    response = client.post('/suppliers/',
                           headers=admin_auth_header,
                           json={'name': 'LG'})
    assert response.status_code == 201

    response = client.put('/suppliers/1',
                          headers=admin_auth_header,
                          json={'name': 'Samsung'})
    assert response.status_code == 200

    response = client.get(
        '/suppliers/1', headers=admin_auth_header)
    assert response.json()['name'] == 'Samsung'
