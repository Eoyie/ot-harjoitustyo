import os
import shutil
from config import MAIN_FILE_PATH

class UserRepository:
    """Käyttäjien tietokantaoperaatiosta vastaava luokka."""
    def __init__(self, dirname, ):
        """Luokan konstruktori.

        Args:
            dirname: Polku tiedostoon, johon käyttäjän tiedostot luodaan.
        """

        self.dirname = dirname

    def make_user_folder(self, username):
        """Luo kansion uudelle käyttäjälle.
        
        Args:
            username: Käyttäjän username
        Returns:
            Vahvistuksen siitä, onko kansio olemassa"""
        res = self.ensure_user_folder_exists(username)
        if res is True:
            return False
        
        path = os.path.join(self.dirname, username)
        os.mkdir(path)

        return self.ensure_user_folder_exists(username)

    def ensure_user_folder_exists(self, username):
        """Tarkistaa käyttäjän kansion olemassa olon.

        Args:
            username: Käyttäjän username
        Returns:
            Vahvistuksen siitä, onko kansio olemassa"""

        user_folders = [x[0] for x in os.walk(self.dirname)]

        for folder in user_folders:
            folder_name = os.path.basename(os.path.normpath(folder))
            if username == folder_name:
                return True
        return False

    def give_all_users(self):
        """Palauttaa kaikki käyttäjät
         
        Returns:
            Lista käyttäjistä"""

        user_folders = [x[0] for x in os.walk(self.dirname)]
        user_list = []

        for folder in user_folders:
            folder_name = os.path.basename(os.path.normpath(folder))
            if folder_name == 'data':
                pass
            else:
                user_list.append(folder_name)
        return user_list

    def delete_user(self,user):
        """Poistaa käyttäjän
        
        Arg:
            Käyttäjän nimi"""
        shutil.rmtree(self.dirname + "/" +user)


user_repository = UserRepository(MAIN_FILE_PATH)
