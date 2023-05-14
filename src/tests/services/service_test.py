import unittest
from entities.exp import Exp
from services.exp_service import ExpService

class TestExpService(unittest.TestCase):
    def setUp(self): 
        self.exp_service = ExpService(FakeExpRepository())

    def test_adding_product(self):
        self.exp_service.add_product('This is a test!','20-02-2002',1,1)
        products = self.exp_service.get_all_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

    def test_delete_product(self):
        a = self.exp_service.add_product('This is a test!','20-02-2002',1,1)
        b = self.exp_service.add_product('This is a test2!','20-02-2002',1,2)
        self.exp_service.delete_product(b.id)
        products = self.exp_service.get_all_products()

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product, 'This is a test!')

    def test_delete_all(self):
        a = self.exp_service.add_product('This is a test!','20-02-2002',1,1)
        b = self.exp_service.add_product('This is a test2!','20-02-2002',1,2)
        self.exp_service.delete_all()
        products = self.exp_service.get_all_products()

        self.assertEqual(len(products), 0)

    def test_make_user(self):

        self.assertTrue(self.exp_service.create_user("haha"))
        self.assertFalse(self.exp_service.create_user("haha"))

        self.exp_service.create_user("haha")

    def test_delete_user(self):
        self.exp_service.create_user("haha")
        all = self.exp_service.get_all_users()
        self.exp_service.delete_user("haha")
        non = self.exp_service.get_all_users()
        self.assertEqual(len(all)-1,len(non))
        

class FakeExpRepository:
    def __init__(self, products = None):
        self.products = products or []
        self.users = []

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

    
    def delete_all(self):
        self.products=[]
    
    def make_user_folder(self,username):
        if username not in self.users:
            self.users.append(username)
            return True
        return False

    def ensure_user_folder_exists(self,username):
        if username not in self.users:
            return True
        return False
    
    def delete_user(self,username):
        self.users.pop(username)

    def give_all_users(self):
        return self.users