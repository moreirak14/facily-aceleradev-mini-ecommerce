from fastapi.testclient import TestClient


def test_product_discount_create_is_enabled(client: TestClient, admin_auth_header, product_factory, payment_method_factory):
    product = product_factory(visible=True)
    payment_method = payment_method_factory(enabled=False)

    response = client.post('/payment_discounts/',
                           headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_methods_id': payment_method.id,
                           })
    assert response.status_code == 400
    assert response.json()['detail'] == "This payment method is not available"


def test_product_discount_create(client: TestClient, admin_auth_header, product_factory, payment_method_factory):
    product = product_factory(visible=True)
    payment_method = payment_method_factory(enabled=True)
    
    response = client.post('/payment_discounts/',
                           headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_methods_id': payment_method.id,
                           })
    assert response.status_code == 201


def test_product_discount_delete(client: TestClient, admin_auth_header, product_factory, payment_method_factory):
    product = product_factory(visible=True)
    payment_method = payment_method_factory(enabled=True)

    response = client.post('/payment_discounts/',
                           headers=admin_auth_header,
                           json={
                               'mode': 'value',
                               'value': 10,
                               'product_id': product.id,
                               'payment_methods_id': payment_method.id,
                           })
    assert response.status_code == 201

    id = response.json()['id']
    response = client.delete(f'/payment_discounts/{id}', 
                             json={'id': 'pyint'})
    assert response.status_code == 202
