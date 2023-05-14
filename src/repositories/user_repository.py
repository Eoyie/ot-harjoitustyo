import os
import sqlite3
from entities.user import User
from config import MAIN_FILE_PATH, DATABASE_FILE_PATH
from database_connection import get_database_connection

class UserRepository:
    """Käyttäjien tietokantaoperaatiosta vastaava luokka."""
    def __init__(self, dirname, _connection):
        """Luokan konstruktori.

        Args:
            dirname: Polku tiedostoon, johon käyttäjän tiedostot luodaan.
            _connection: Tietokantayhteyden _connection-olio.
        """

        self.dirname = dirname
        self._connection  = sqlite3.connect(DATABASE_FILE_PATH)

    def make_user_folder(self, username):
        """Luo kansion uudelle käyttäjälle.
        
        Args:
            username: Käyttäjän username
        Returns:
            Vahvistuksen siitä, onko kansio olemassa"""
        
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
    
    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan käyttäjistä User-olioina.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))
    

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
        Returns:
            Palauttaa User-olion, halutusta käyttäjästä.
            Jos ei löydy niin palauttaa None.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?",
                       (username,))
        row = cursor.fetchone()
    
        return User(row[0], row[1]) if row else None
    
    def create(self, user):
        """Tallentaa käyttäjän SQL-tietokantaan.

        Args: 
            user: Tallennettava käyttäjä User-oliona.
        Returns:
            sama User-olio.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user
    
    def delete_all(self):
        """Poistaa kaikki käyttäjät."""
        cursor = self._connection.cursor()
        cursor.execute("delete from users")

        self._connection.commit()

user_repository = UserRepository(MAIN_FILE_PATH, get_database_connection)