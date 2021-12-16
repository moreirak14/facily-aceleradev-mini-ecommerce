from fastapi.testclient import TestClient


def test_coupon_create(client: TestClient, admin_auth_header, coupon_factory):
    response = client.post('/coupons/',
                           headers=admin_auth_header,
                           json={
                               'code': '1234CODE',
                               'expire_at': '2021-12-15T23:42:20.154Z',
                               'limit': 10,
                               'type': 'value',
                               'value': 200
                           })
    assert response.status_code == 201

    response = client.get(
        '/coupons/1', headers=admin_auth_header)
    assert response.json()['code'] == '1234CODE'

    response = client.post('/coupons/',
                           headers=admin_auth_header,
                           json={
                               'code': '1234CODE',
                               'expire_at': '2021-12-15T23:42:20.154Z',
                               'limit': 10,
                               'type': 'value',
                               'value': 200
                           })
    assert response.status_code == 500
    assert response.json()[
        'detail'] == "There is already a coupon with the same code"


def test_coupon_update(client: TestClient, admin_auth_header):
    response = client.post('/coupons/',
                           headers=admin_auth_header,
                           json={
                               'code': '1234CODE',
                               'expire_at': '2021-12-15T23:42:20.154Z',
                               'limit': 10,
                               'type': 'value',
                               'value': 200
                           })
    assert response.status_code == 201

    response = client.put('/coupons/1',
                          headers=admin_auth_header,
                          json={
                              'expire_at': '2021-12-15T23:52:09.950000',
                              'limit': 15
                          })
    assert response.status_code == 202

    response = client.get(
        '/coupons/1', headers=admin_auth_header)
    assert response.json()['code'] == '1234CODE'


def test_coupon_delete(client: TestClient, admin_auth_header):
    response = client.post('/coupons/',
                           headers=admin_auth_header,
                           json={
                               'code': '1234CODE',
                               'expire_at': '2021-12-15T23:42:20.154Z',
                               'limit': 10,
                               'type': 'value',
                               'value': 200
                           })
    assert response.status_code == 201

    response = client.get(
        '/coupons/1', headers=admin_auth_header)
    assert response.json()['code'] == '1234CODE'
    id = response.json()['id']

    response = client.delete(f'/coupons/{id}',
                             headers=admin_auth_header,
                             json={'id': 'pyint'})
    assert response.status_code == 202
