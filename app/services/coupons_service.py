from datetime import datetime
from app.repositories.cupons_repository import CouponsRepository
from app.api.coupons.schemas import ShowCouponsSchema, UpdateCoupons
from fastapi import Depends
from app.models.models import Coupons
from app.common.exceptions import CouponsCodeAlreadyExistsException, CouponsExpire


class CouponsService:
    def __init__(self, coupons_repository: CouponsRepository = Depends()):
        self.coupons_repository = coupons_repository

    """ --> a variavel coupons_code percorre todo o model de coupons e retorna valor de code """
    def create_coupons(self, coupons: ShowCouponsSchema):
        coupons_code = self.coupons_repository.filter({"code": coupons.code}) # --> retorna valor code
        if coupons_code: # --> se coupons_code já existir retorna exception
            raise CouponsCodeAlreadyExistsException()
        
        """ --> cria cupom caso não exista outro codigo """
        self.coupons_repository.create(Coupons(**coupons.dict()))

    # def update_coupons(self, id: int, update: UpdateCoupons):
    #     update_field_expire = self.coupons_repository.filter({"expire_at": update.expire_at.now})
        
    #     if update_field_expire:
    #         raise CouponsExpire()
        
    #     self.coupons_repository.update(Coupons(**update.dict()))
