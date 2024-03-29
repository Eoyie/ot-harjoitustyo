from entities.exp import Exp

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

    def create_user(self, username):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka on käyttäjän username."""
        result = self.user_repository.ensure_user_folder_exists(username)
        if result is True:
            return False

        self.user_repository.make_user_folder(username)
        return self.user_repository.ensure_user_folder_exists(username)

    def login(self, username):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka on kirjautuvan käyttäjän username.
        """

        return self.user_repository.ensure_user_folder_exists(username)

    def get_all_users(self):
        """Hakee kaikki käyttäjät
        
        Returns:
            Kaikki käyttäjät listassa"""

        return self.user_repository.give_all_users()

    def delete_user(self,user):
        """Poistaa käyttäjän
        
        Args:
            Käyttäjän nimi"""

        self.user_repository.delete_user(user)

    def update_file_path(self, username):

        self.exp_repository.update_file_path(username)

    def get_all_products(self):
        """Palauttaa kaikki tuotteet.
        
        Returns: Palauttaa kaikki tuotteet listana"""

        products = self.exp_repository.find_all()

        return products

    def get_one_product(self, p_id):
        """Palauttaa halutun tuotteen.
        
        Returns: Tuotteen listana"""

        return self.exp_repository.find_one(p_id)

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

    def update_one(self, product, date, qty, p_type, old_p_id):
        """Päivittää yhden tuotteen tiedot.

        Args:
            product: Merkkijonoarvo, joka on tuote.
            date: Merkkijonoarvo, joka on tuotteen viim. käyttöpäivä.
            qty: Merkkijonoarvo, joka on tuotteen määrä.
            p_type: Merkkijonoarvo, joka kertoo tuotteen tyypistä.
            old_p_id: Merkkijonoarvo, joka on päivitettävän tuotteen vanha id.
        """

        product = Exp(product, date, qty, p_type, old_p_id)

        self.exp_repository.update(product, old_p_id)

    def delete_product(self, p_id):
        """Poistaa yhden tuotteen.
        
        Args:
            p_id: Merkkijonoarvo, joka on poistettavan tuotteen id"""
        self.exp_repository.delete_product(p_id)

    def delete_all(self):
        """Poistaa kaikki tuotteet."""

        self.exp_repository.delete_all()

    def set_product_expired(self, p_id, p_qty):
        """Laittaa tuotteen tilan vanhentuneeksi.
        
        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
            p_qty: Merkkijonoarvo, joka kuinka suuri osa tuotteesta muutetaan
        Returns:
            Saman tuotteen, jonka tila on päivitetty vanhentuneeksi"""
        self.exp_repository.set_expired(p_id, p_qty)

    def set_product_used(self, p_id, p_qty):
        """Laittaa tuotteen tilan käytetyksi.
        
        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
            p_qty: Merkkijonoarvo, joka kuinka suuri osa tuotteesta muutetaan
        Returns:
            Saman tuotteen, jonka tila on päivitetty käytetyksi"""
        self.exp_repository.set_used(p_id, p_qty)

    def automatic_expire(self):
        """Päivittää tuotteiden vanhentumiset päivämäärän mukaan.
        
        Returns:
            Päivitetyt tuotteet listassa Exp-oliona"""
        del_products = self.exp_repository.automatic_expire()

        if del_products:
            for product_id in del_products:
                self.delete_product(product_id)

exp_service = ExpService()
