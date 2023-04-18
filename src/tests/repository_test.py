import unittest
from repositories.expire_repository import exp_repository
from entities.exp import Exp

class TestExpRepository(unittest.TestCase):
    def setUp(self):
        exp_repository.delete_all()

        self.maito = Exp('Maito')
        self.leipa = Exp('Leipä')

    def test_add_product(self):
        exp_repository.create(self.maito)
        products = exp_repository.find_all()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'Maito')

    def test_delete_product(self):
        exp_repository.create(self.maito)
        exp_repository.create(self.leipa)
        exp_repository.delete_product(1)
        products = exp_repository.find_all()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'Maito')