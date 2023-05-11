import os
from entities.user import User
from config import MAIN_FILE_PATH


class UserRepository:

    def __init__(self, dirname):

        self.dirname = dirname
        self.current_user = None

    def make_user_folder(self, username):
        
        path = os.path.join(self.dirname, username)
        os.mkdir(path)

    def ensure_user_folder_exists(self, username):

        user_folders = [x[0] for x in os.walk(self.dirname)]

        for folder in user_folders:
            folder_name = os.path.basename(os.path.normpath(folder))
            if username == folder_name:
                return True
        return False

user_repository = UserRepository(MAIN_FILE_PATH)