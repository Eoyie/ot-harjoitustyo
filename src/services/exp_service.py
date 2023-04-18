from entities.exp import Exp

from repositories.expire_repository import (
    exp_repository as default_exp_repository )

class ExpService:

    def __init__(self, exp_repository = default_exp_repository):
        self.exp_repository = exp_repository

    def add_product(self, product):#, type, date):

        product = Exp(product=product)#, type=type, date=date)

        return self.exp_repository.create(product)

    def get_ok_products(self):

        products = self.exp_repository.read2()
        #ok_products = filter(lambda product: not product.expired, products)

        return products

    def set_product_expired(self, exp_id):
        self.exp_repository.set_expired(exp_id)

    def delete_product(self, product_num):

        self.exp_repository.delete_product(product_num)

exp_service = ExpService()
