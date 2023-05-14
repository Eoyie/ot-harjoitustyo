import unittest
from repositories.user_repository import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.username = "Janne"

    def test_make_file(self):
        response = user_repository.make_user_folder(self.username)

        self.assertTrue(response)
        user_repository.delete_user(self.username)

    def test_no_same_users(self):
        user_repository.make_user_folder(self.username)
        response = user_repository.make_user_folder(self.username)
    
        self.assertFalse(response)
        user_repository.delete_user(self.username)

    def test_get_all_users_works(self):
        user_repository.make_user_folder(self.username)
        amount = user_repository.give_all_users()

        user_repository.delete_user(self.username)
        second_amount = user_repository.give_all_users()

        self.assertEqual(len(amount)-1,len(second_amount))