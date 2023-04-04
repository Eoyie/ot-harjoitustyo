import unittest
from expire import Expire

class TestExpire(unittest.TestCase):
    def setUp(self):
        self.expire = Expire()
    
    def test_expire_list_exists(self):
        self.assertNotEqual(self.expire,None)
    
    def test_expire_list_add_one_works(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])

        self.assertEqual(len(self.expire.exp_repository),1)
    
    def test_can_add_multiple(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])
        self.expire.add_product([2,"Juusto", 1, "2023-04-05",0])
        self.expire.add_product([3,"Jugurtti", 1, "2023-04-05",0])

        self.assertEqual(len(self.expire.exp_repository),3)
    
    def test_delete_product_works(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])
        self.expire.add_product([2,"Juusto", 1, "2023-04-05",0])
        self.expire.add_product([3,"Jugurtti", 1, "2023-04-05",0])
        self.assertEqual(len(self.expire.exp_repository),3)

        self.expire.delete_product("Juusto")
        self.assertEqual(len(self.expire.exp_repository),2)    
    
    def test_delete_all_works(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])
        self.expire.add_product([2,"Juusto", 1, "2023-04-05",0])
        self.expire.add_product([3,"Jugurtti", 1, "2023-04-05",0])
        self.expire.delete_all()

        self.assertEqual(len(self.expire.exp_repository),0)

    def test_can_change_status(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])
        self.expire.spoiled_product("Maito")

        self.assertEqual(self.expire.exp_repository[0][4], 1)

    def test_status_nothing_to_change(self):
        self.expire.add_product([1,"Maito", 1, "2023-04-05",0])
        self.expire.spoiled_product("Juusto")

        self.assertEqual(self.expire.exp_repository[0][4], 0)