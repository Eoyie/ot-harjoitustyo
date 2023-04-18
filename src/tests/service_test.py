import unittest
from entities.exp import Exp
from services.exp_service import ExpService

class TestExpService(unittest.TestCase):
    def setUp(self):
        self.exp_service = ExpService(FakeExpRepository())

    def test_adding_product(self):
        self.exp_service.add_product('This is a test!')
        products = self.exp_service.get_ok_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

    def test_delete_product(self):
        self.exp_service.add_product('This is a test!')
        self.exp_service.add_product('This is a test2!')
        self.exp_service.delete_product(1)
        products = self.exp_service.get_ok_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

class FakeExpRepository:
    def __init__(self, products = None):
        self.products = products or []

    def create(self, product):
        self.products.append(product)
        return product

    def read2(self):
        return self.products

    def delete_product(self, product_num):
        products_left = []
        for i in range(len(self.products)):
            if i != product_num:
                products_left.append(self.products[i])

        self.products = products_left