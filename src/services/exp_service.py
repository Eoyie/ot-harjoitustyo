from entities.exp import Exp
from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository )
from repositories.expire_repository import (
    exp_repository as default_exp_repository )

class ExpService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self,
                 exp_repository = default_exp_repository,
                 user_repository = default_user_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        
        Args:
            exp_repository:
                Vapaaehtoinen, oletusarvoltaan ExpRepository-olio.
                Olio, jolla on ExpRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self.exp_repository = exp_repository
        self.user_repository = user_repository

        self.user = None

    def make_user_folder(self, username):

        self.user_repository.make_user_folder(username)

    def ensure_user_folder_exists(self, username):

        return self.user_repository.ensure_user_folder_exists(username)
        
    def login(self, username):
        
        response = self.ensure_user_folder_exists(username)
        if response == False:
            return response
        self.set_user(username)

        return response
    
    def set_user(self, username):

        self.user = username

    def update_file_path(self, username):

        self.exp_repository.update_file_path(username)

    def add_product(self, product, date, qty, p_type):
        """Lisää uuden tuotteen.

        Args:
            product: Merkkijonoarvo, joka on tuote.
            date: Merkkijonoarvo, joka on tuotteen viim. käyttöpäivä.
            qty: Merkkijonoarvo, joka on tuotteen määrä.
            p_type: Merkkijonoarvo, joka kertoo tuotteen tyypistä.
        Returns:
            Lisätty tuote Exp-olion muodossa.
        """
        product = Exp(product=product, date=date, qty=qty, p_type=p_type)

        return self.exp_repository.create(product)

    def get_all_products(self):
        """Palauttaa kaikki tuotteet
        
        Returns: Palauttaa kaikki tuotteet listana"""

        products = self.exp_repository.find_all()

        return products

    def delete_product(self, p_id):
        """Poistaa tuotteen
        
        Args:
            p_id: Merkkijonoarvo, joka on poistettavan tuotteen id"""
        self.exp_repository.delete_product(p_id)

    def delete_all(self):
        """Poistaa kaikki tuotteet"""

        self.exp_repository.delete_all()

    def set_product_expired(self, p_id):
        """Laittaa tuotteen tilan vanhentuneeksi
        
        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
        Returns:
            Saman tuotteen, jonka tila on päivitetty vanhentuneeksi"""
        return self.exp_repository.set_expired(p_id)

    def set_product_used(self, p_id):
        """Laittaa tuotteen tilan käytetyksi
        
        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
        Returns:
            Saman tuotteen, jonka tila on päivitetty käytetyksi"""
        return self.exp_repository.set_used(p_id)
    
    def automatic_expire(self):
        
        return self.exp_repository.automatic_expire(self.user)

exp_service = ExpService()
