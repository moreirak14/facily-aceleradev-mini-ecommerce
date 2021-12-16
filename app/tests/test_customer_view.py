from fastapi.testclient import TestClient
import factory


def test_customer_create(client: TestClient, user_factory):
    user = user_factory(id=factory.Faker('pyint'), role='customer')

    response = client.post('/customers/',
                           json={'first_name': 'teste',
                                 'last_name': 'teste da silva',
                                 'phone_number': '123',
                                 'genre': 'm',
                                 'document_id': '123456789',
                                 'birth_date': '1998-05-03',
                                 'user_id': user.id})
    assert response.status_code == 201

    response = client.get('/customers/1')
    assert response.json()['document_id'] == '123456789'


def test_customer_update(client: TestClient, user_factory):
    user = user_factory(id=factory.Faker('pyint'), role='customer')

    response = client.post('/customers/',
                           json={'first_name': 'teste',
                                 'last_name': 'teste da silva',
                                 'phone_number': '123',
                                 'genre': 'm',
                                 'document_id': '123456789',
                                 'birth_date': '1998-05-03',
                                 'user_id': user.id})
    assert response.status_code == 201
    id = response.json()['id']

    response = client.get(f'/customers/{id}')
    assert response.json()['document_id'] == '123456789'

    response = client.put('/customers/',
                           json={'first_name': 'teste',
                                 'last_name': 'teste',
                                 'phone_number': '12645370',
                                 'genre': 'm',
                                 'birth_date': '2021-12-16'})
    assert response.status_code == 202
    
    response = client.get(f'/customers/{id}')
    assert response.json()['last_name'] == 'teste'
    assert response.json()['phone_number'] == '123456789'
