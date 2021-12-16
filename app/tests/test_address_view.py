import factory
from fastapi.testclient import TestClient


def test_address_create_with_customer_zeroed(client: TestClient):  
    response = client.post('/addresses/', json={
        "address": 'rua do fulano',
        "city": 'Aruja',
        "state": 'SP',
        "number": '123',
        "zipcode": '07400888',
        "neighbourhood": 'fofoqueiro',
        "primary": 'true',
        "customer_id": 0
    })
    assert response.status_code == 401
    assert response.json()[
        'detail'] == "The address needs a customer, the value cannot be empty"


def test_address_create(client: TestClient, customer_factory):
    customer = customer_factory(id=factory.Faker('pyint'))

    response = client.post('/addresses/', json={
        "address": 'rua do fulano',
        "city": 'Aruja',
        "state": 'SP',
        "number": '123',
        "zipcode": '07400888',
        "neighbourhood": 'fofoqueiro',
        "primary": 'true',
        "customer_id": customer.id
    })
    assert response.status_code == 201

    response = client.get('/addresses/1')
    assert response.json()['address'] == 'rua do fulano'
    assert response.json()['zipcode'] == '07400888'


def test_address_update(client: TestClient, customer_factory):
    customer = customer_factory(id=factory.Faker('pyint'))

    response = client.post('/addresses/', json={
        "address": 'rua do fulano',
        "city": 'Aruja',
        "state": 'SP',
        "number": '123',
        "zipcode": '07400888',
        "neighbourhood": 'fofoqueiro',
        "primary": 'true',
        "customer_id": customer.id
    })
    assert response.status_code == 201

    response = client.get('/addresses/1')
    assert response.json()['address'] == 'rua do fulano'
    assert response.json()['zipcode'] == '07400888'
    
    id = response.json()['id']
    response = client.put(f'/addresses/{id}', json={
        "address": 'rua da ciclana',
        "city": 'Guarulhos',
        "state": 'SP',
        "number": '321',
        "zipcode": '07176000',
        "neighbourhood": 'fofoqueira',
        "primary": 'true',
        "customer_id": customer.id
    })
    assert response.status_code == 202

    response = client.get(f'/addresses/{id}')
    assert response.json()['address'] == 'rua da ciclana'
    assert response.json()['zipcode'] == '07176000'


def test_address_delete(client: TestClient, customer_factory):
    customer = customer_factory(id=factory.Faker('pyint'))

    response = client.post('/addresses/', json={
        "address": 'rua do fulano',
        "city": 'Aruja',
        "state": 'SP',
        "number": '123',
        "zipcode": '07400888',
        "neighbourhood": 'fofoqueiro',
        "primary": 'true',
        "customer_id": customer.id
    })
    assert response.status_code == 201

    response = client.get('/addresses/1')
    assert response.json()['address'] == 'rua do fulano'
    assert response.json()['zipcode'] == '07400888'

    id = response.json()['id']
    response = client.delete(f'/addresses/{id}', json={'id': 'pyint'})
    assert response.status_code == 202
