from entities.exp import Exp

from repositories.expire_repository import (
    exp_repository as default_exp_repository )

class ExpService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, exp_repository = default_exp_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        
        Args:
            exp_repository:
                Vapaaehtoinen, oletusarvoltaan EXPRepository-olio.
                Olio, jolla on EXPRepository-luokkaa vastaavat metodit.
        """
        self.exp_repository = exp_repository

    def add_product(self, product, date, p_type):
        """Lisää uuden tuotteen.

        Args:
            product: Merkkijonoarvo, joka on tuote.
            date: Merkkijonoarvo, joka on tuotteen viim. käyttöpäivä.
            p_type: Intergerarvo, joka kertoo tuotteen tyypistä.
        Returns:
            Lisätty tuote Exp-olion muodossa.
        """
        product = Exp(product=product, date=date, p_type=p_type)

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


exp_service = ExpService()
