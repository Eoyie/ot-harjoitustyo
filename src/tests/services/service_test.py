import unittest
from entities.exp import Exp
from services.exp_service import ExpService

class TestExpService(unittest.TestCase):
    def setUp(self):
        self.exp_service = ExpService(FakeExpRepository())

    def test_adding_product(self):
        self.exp_service.add_product('This is a test!','20-02-2002',1)
        products = self.exp_service.get_all_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

    def test_delete_product(self):
        a = self.exp_service.add_product('This is a test!','20-02-2002',1)
        b = self.exp_service.add_product('This is a test2!','20-02-2002',2)
        self.exp_service.delete_product(b.id)
        products = self.exp_service.get_all_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

class FakeExpRepository:
    def __init__(self, products = None):
        self.products = products or []

    def create(self, product):
        self.products.append(product)
        return product

    def find_all(self):
        return self.products

    def delete_product(self, p_id):
        products_left = []
        for i in self.products:
            if i.id != p_id:
                products_left.append(i)

        self.products = products_left