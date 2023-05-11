import uuid

class Exp:
    """Luokka, joka kuvaa yksittäistä tuotetta

    Attributes:
        product: Merkkijonoarvo, joka on tuote.
        date: Merkkijonoarvo, joka on tuotteen viim. käyttöpäivä.
        qty: Merkkijonoarvo, joka on tuotteen määrä.
        p_type: Merkkijonoarvo, joka kertoo tuotteen tyypistä.
        p_id: Merkkijonoarvo, joka on tuotteen id.
    """
    def __init__(self, product, date, qty, p_type, p_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän
        
        Kirjoitan myöhemmin~"""
        self.id = p_id or str(uuid.uuid4())
        self.product = product
        self.date = date
        self.qty = qty
        self.type = p_type
