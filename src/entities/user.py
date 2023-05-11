import uuid

class User:
    """Luokka, joka kuvaa yksittäistä tuotetta

    Attributes:
        product: Merkkijonoarvo, joka on käyttäjän username.
    """
    def __init__(self, username, u_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän
        
        Kirjoitan myöhemmin~"""
        self.username = username
        self.id = u_id or str(uuid.uuid4())
