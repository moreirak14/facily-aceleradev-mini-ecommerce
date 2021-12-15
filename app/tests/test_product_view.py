from fastapi.testclient import TestClient


def test_product_create(client: TestClient, supplier_factory, category_factory, admin_auth_header):
    # --> instancia a factory de categorie e supplier do arquivo conftest
    category = category_factory()
    supplier = supplier_factory()

    response = client.post('/products/',
                           headers=admin_auth_header,
                           json={
                               'description': 'descricao',
                               'price': '100',
                               'technical_details': 'bla bla bla',
                               'image': 'image.dev',
                               'visible': True,
                               'categorie_id': category.id,
                               'supplier_id': supplier.id
                           })
    assert response.status_code == 201

    response = client.get(
        '/products/1', headers=admin_auth_header)
    assert response.json()['description'] == 'descricao'
    assert response.json()['categorie_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id
