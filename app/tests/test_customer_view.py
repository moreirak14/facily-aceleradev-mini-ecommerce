from fastapi.testclient import TestClient


def test_customer_create(client: TestClient):
    response = client.post('/customers/',
                           json={'first_name': 'teste',
                                 'last_name': 'teste da silva',
                                 'phone_number': '123',
                                 'genre': 'm',
                                 'document_id': '123456789',
                                 'birth_date': '1998-05-03',
                                 'user': {
                                     "display_name": "userteste",
                                     "email": "userteste@email.com",
                                     "password": "123"
                                 }})
    assert response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['document_id'] == '123456789'


def test_customer_update(client: TestClient, user_factory, customer_factory):
    user = user_factory(role='customer')
    customer = customer_factory(user_id=user.id)

    response = client.post('/customers/',
                           json={'first_name': 'teste',
                                 'last_name': 'teste da silva',
                                 'phone_number': '123',
                                 'genre': 'm',
                                 'document_id': '123456789',
                                 'birth_date': '1998-05-03',
                                 'user': {
                                     "display_name": "userteste",
                                     "email": "userteste@email.com",
                                     "password": "123"
                                 }})
    assert response.status_code == 201
    assert response.json()['id'] == 1
    assert response.json()['document_id'] == '123456789'

    response = client.put(f'/customers/{customer.id}',
                          json={'first_name': 'teste123',
                                'last_name': 'teste123',
                                'phone_number': '12645370',
                                'genre': 'm',
                                'birth_date': '2021-12-16',
                                'user': {
                                    "display_name": "userteste",
                                    "email": "userteste@email.com",
                                    "password": "123",
                                    "id": user.id
                                }})
    assert response.status_code == 202
