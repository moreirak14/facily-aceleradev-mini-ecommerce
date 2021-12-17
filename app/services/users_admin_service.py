from fastapi import Depends
from app.repositories.users_repository import UsersRepository
from app.api.users_admin.schemas import AdminUsersSchema
from app.common.exceptions import EmailAdminUserAuthentication
from app.models.models import User
import bcrypt


class User_dto:
    def __init__(self, display_name, email, password):
        self.display_name = display_name
        self.email = email
        self.password = password

    def dict(self):
        return {'display_name': self.display_name, 'email': self.email, 'password': self.password}


class UsersAdminService:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    def is_valid_email(self, id, email):
        if id != None:
            same_email = self.usersRepository.get_by_id(id)
            if same_email.email == email:
                return True
        if not self.usersRepository.find_by_email(email):
            return True
        raise EmailAdminUserAuthentication()

    def generate_password(self, password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

    def create_admin_user(self, user: User_dto):
        if self.is_valid_email(None, user.email):
            user.password = self.generate_password(user.password)
            userdata = user.dict()
            userdata.update({'role': 'admin'})
            return self.usersRepository.create(User(**userdata))

    def create_customer_user(self, user: User_dto):
        if self.is_valid_email(None, user.email):
            user.password = self.generate_password(user.password)
            userdata = user.dict()
            userdata.update({'role': 'costumer'})
            return self.usersRepository.create(User(**userdata))

    def update_admin_user(self, id, admin_user: AdminUsersSchema):
        if self.is_valid_email(id, admin_user.email):
            admin_user.password = self.generate_password(admin_user.password)
            return self.usersRepository.update(id, admin_user.dict())
