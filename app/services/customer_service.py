from fastapi.param_functions import Depends
from app.repositories.customers_repository import CustomersRepository
from app.api.customers.schemas import CustomersSchema, UpdateCustomersSchema
from app.models.models import Customer
from app.repositories.users_repository import UsersRepository
from app.services.users_admin_service import UsersAdminService, User_dto


class CustomerService:
    def __init__(self, customerRepository: CustomersRepository = Depends(),
                 usersRepository: UsersRepository = Depends(),
                 usersAdminService: UsersAdminService = Depends()):

        self.customerRepository = customerRepository
        self.usersRepository = usersRepository
        self.usersAdminService = usersAdminService

    def create_customer(self, customer: CustomersSchema):
        user_create = self.usersAdminService.create_customer_user(
            User_dto(**customer.user.dict()))
        customer_data = customer.dict()
        customer_data.pop('user')
        customer_data.update({'user_id': user_create.id})
        return self.customerRepository.create(Customer(**customer_data))

    def update_customer(self, id: int, customer: UpdateCustomersSchema):
        customer_data = customer.dict()
        user_data = customer_data.pop('user')
        customer_model = self.customerRepository.update(id, customer_data)
        self.usersRepository.update(user_data['id'], user_data)
        return customer_model
