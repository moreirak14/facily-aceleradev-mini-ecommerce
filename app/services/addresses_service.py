from fastapi import Depends
from app.repositories.addresses_repository import AddressesRepository
from app.api.addresses.schemas import ShowAddressesSchema
from app.models.models import Address
from app.common.exceptions import CustomersInvalidNone


class AddressesService:
    def __init__(self, addresses_repository: AddressesRepository = Depends()):
        self.addresses_repository = addresses_repository

    def is_primary(self, addresses: ShowAddressesSchema):
        primary = self.addresses_repository.filter_by(
            {"primary": addresses.primary, "customer_id": addresses.customer_id})

        if primary:
            self.addresses_repository.update(primary.id, {"primary": False})

    def costumer_id(self, addresses: ShowAddressesSchema):
        return self.addresses_repository.filter({"customer_id": addresses.customer_id})

    def create_address(self, addresses: ShowAddressesSchema):
        if addresses.customer_id == 0:
            raise CustomersInvalidNone()

        if addresses.primary:
            self.is_primary(addresses)

        self.addresses_repository.create(Address(**addresses.dict()))
