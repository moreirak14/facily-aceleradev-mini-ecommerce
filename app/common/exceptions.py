""" --> mensagem de retorno de avaliação de metodos de pagamentos. """
class PaymentMethodsNotAvailableException(Exception):
    def __init__(self):
        self.message = 'This payment method is not available'
        super().__init__(self.message)


""" --> mensagem de retorno se já existe desconto atribuido em produto. """
class PaymentMethodDiscountAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a discount with this payment method'
        super().__init__(self.message)


""" --> mensagem de retorno se já existe algum codigo no banco. """
class CouponsCodeAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'There is already a coupon with the same code'
        super().__init__(self.message)


class CouponsExpire(Exception):
    def __init__(self):
        self.message = 'This coupon has an expired date'
        super().__init__(self.message)
