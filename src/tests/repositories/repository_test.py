import unittest
from repositories.expire_repository import exp_repository
from entities.exp import Exp 

class TestExpRepository(unittest.TestCase):
    def setUp(self):
        exp_repository.update_file_path("test")
        self.n = len(exp_repository.find_all())

        self.maito = Exp('Maito',"20-02-2024","5","0")
        self.leipa = Exp('Leipä',"02-12-2020","1","2")

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
    
    def test_find_product(self):

        exp_repository.create(self.maito)

        product = exp_repository.find_one(self.maito.id)

        self.assertEqual(self.maito.id, product.id)

        exp_repository.delete_product(self.maito.id)

    def test_find_no_product(self):
        product = exp_repository.find_one(self.maito.id)
        self.assertFalse(product)
    
    def test_set_expired(self):
        maito = exp_repository.create(self.maito)
        
        exp_repository.set_expired(maito.id,1)
        product = exp_repository.find_one(maito.id)

        self.assertEqual(int(maito.qty)-1, int(product.qty))

        exp_repository.delete_all()

    def test_set_used(self):
        maito = exp_repository.create(self.maito)
        
        exp_repository.set_expired(self.maito.id,1)

        product = exp_repository.find_one(maito.id)

        self.assertEqual(int(self.maito.qty)-1, int(product.qty))


        exp_repository.delete_all()

    def test_automatic_expire(self):

        exp_repository.create(self.maito)
        del_p = exp_repository.automatic_expire()
        
        self.assertEqual(len(del_p),0)

        exp_repository.delete_all()


