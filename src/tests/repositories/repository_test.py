import unittest
from repositories.expire_repository import exp_repository
from entities.exp import Exp

class TestExpRepository(unittest.TestCase):
    def setUp(self):
        self.n = len(exp_repository.find_all())

        self.maito = Exp('Maito',"20-02-2002",0)
        self.leipa = Exp('Leipä',"02-12-2020",2)

    def test_add_product(self):
        exp_repository.create(self.maito)
        products = exp_repository.find_all()

        self.assertEqual(len(products), (self.n+1))
        self.assertEqual(products[0].product, 'Maito')
        exp_repository.delete_product(self.maito.id)

    def test_delete_product(self):
        exp_repository.create(self.maito)
        exp_repository.create(self.leipa)
        exp_repository.delete_product(self.leipa.id)
        products = exp_repository.find_all()

        self.assertEqual(len(products), (self.n+1))
        self.assertEqual(products[0].product, 'Maito')

        exp_repository.delete_product(self.maito.id)
        products = exp_repository.find_all()

        self.assertEqual(len(products), self.n)