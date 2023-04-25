from entities.exp import Exp

from repositories.expire_repository import (
    exp_repository as default_exp_repository )

class ExpService:

    def __init__(self, exp_repository = default_exp_repository):
        self.exp_repository = exp_repository

    def add_product(self, product, date, p_type):
        product = Exp(product=product, date=date, p_type=p_type)

        return self.exp_repository.create(product)

    def get_all_products(self):
        products = self.exp_repository.find_all()

        return products

    def delete_product(self, p_id):
        self.exp_repository.delete_product(p_id)

    def set_product_expired(self, p_id):
        return self.exp_repository.set_expired(p_id)

    def set_product_used(self, p_id):
        return self.exp_repository.set_used(p_id)


exp_service = ExpService()
