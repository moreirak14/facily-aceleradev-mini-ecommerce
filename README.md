# facily-aceleradev-mini-ecommerce

Tarefa 1:
Criar um CRUD completo para as entidades Category, Supplier e PaymentMethods. A estrutura de pastas das rotas deverá ser a mesma da que fizemos junto para a entidade Product. Não precisa criar os relacionamentos nesse primeiro momento . OBS: Nenhuma dessas entidades podem ser removidas.

Tarefa 2:
Criar um CRUD para a entidade ProductDiscount.
Crie o relacionamento como mostra o diagrama em anexo (entre Product e PaymentMethod) 
As seguintes regras deverão ser aplicadas:
1 - O campo mode só poderá receber os valores: value ou percentage (faça esta validação no Schema do pydantic)
2 - Só poderá existir um desconto pra cada tipo de forma de pagamento
3 - Não poderá ser criado o desconto se a forma de pagamento estiver desabilitada
Descontos podem ser removidos

Tarefa 3:
Refatore as views para que acessem a camada Repository para efetuar as operações. Para cada entidade crie um Repository, que estenda de BaseRepository. Use o ProductRepository como exemplo. Crie também a camada Service quando necessário (quando houver alguma regra de negócio precisar ser feita antes de persistir a entidade).

Tarefa 4:
Criar um CRUD para a entidade Coupons.
As seguintes regras deverão ser aplicadas:
1 - O código do cupom deverá ser informado, mas deverá ser único
2 - O campo type  só poderá receber os valores: value ou percentage (faça esta validação no Schema do pydantic)
3 - Somente os campos limit e expire_at poderão ser alterados
Cupons podem ser removidos

Tarefa 5:
Criar um CRUD para as entidades e o relacionamento de Customer e Address.
Somente o campo document_id (este campo é como se fosse o CPF) não poderá ser alterado
Não precisa criar o relacionamento com User
Endereços podem ser removidos
Consumidores podem ter mais de um endereço, mas somente um deles pode ser primário. Ao cadastrar um novo e este estiver como primário, o existente deixará de ser.

Tarefa 6:
De acordo com o que foi mostrado em aula, faça com que os CRUDs da entidades Product, Category, Supplier, PaymentMethods, ProductDiscounts e Coupons sejam protegidos por autenticação e ainda habilitados somente para usuário com o role=admin

Tarefa 7:
Criar um CRUD para admins, salvando os dados na tabela User. Faça a validação para não existir um usuário com o mesmo email, tanto na criação quanto na atualização. 
Somente usuário com o role=admin pode interagir com este CRUD 
Admins podem ser removidos

Tarefa 8:
Faça o relacionamento entre Customer e User. Faça a alteração no método de criação do customer pra que um user seja criado. Deverá ser valido se o email não está em uso, tanto na criação quanto na atualização. Na criação do usuário, este deve ter o campo role com valor de customer

Tarefa 9:
A ordem (order) representa uma compra feita pelo cliente (customer). Ela possui as informações sobre: forma de pagamento, endereço de entrega, valor total, valor total de desconto.
A criação da ordem deve ser feita por um usuário com o role=customer
O número da ordem deverá ser gerado randomicamente.
O status inicial da ordem deverá ser ORDER PLACED
O campo total_value é a soma do valor de todos os produtos (levando a quantidade do produto em consideração)
O campo total_discount é o valor de desconto em cima do valor total da ordem 
Ao processar a ordem, algumas validações deverão ser feitas:
1 - Da aplicação de desconto: Descontos não são acumulativos. Cupom de desconto tem precedência sobre o desconto pela forma de pagamento. O desconto pela forma de pagamento só pode ser aplicado caso a ordem possua somente aquele produto a qual o desconto está vinculado.
2 - Da validação do cupom: Deve ser verificado se ele não está expirado e/ou se chegou no seu limite de uso. 
3 - Da atualização do status: Só poderá ser feita pelo admin. Toda vez que o status for alterado, esse novo status deverá ser salvo na tabela order_statuses. Para fins de histórico. Os possíveis status são: ORDER PLACED, ORDED PAID, ORDER SHIPPED, ORDER RECEIVED, ORDER COMPLETED, ORDER CANCELLED
Ordens não podem ser excluídas
Ordens não podem ser alteradas
Crie endpoints para listar todas as ordens, como também para trazer os dados de uma ordem

Tarefa 10
Implemente testes nos endpoints que foram construídos até a atividade 9

# _____________________________________

venv
fastapi
sqlalchemy
alembic
pip install alembic
alembic init alembic
alembic revision --autogenerate -m <descricao da minha migration>
alembic upgrade head
alembic downgrade <id da versao>

# adicionar a base em env.py e alembic.ini
from app.models.models import Base
target_metadata = Base.metadata
sqlalchemy.url = sqlite:////home/kaique/Projects/test/facily-aceleradev-mini-ecommerce/app/db/database.db

pip install pytest
pip install response
pip install factory boy