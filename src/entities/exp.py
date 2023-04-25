import uuid

class Exp:
    def __init__(self, product, date, p_type, p_id=None):
        self.id = p_id or str(uuid.uuid4())
        self.product = product
        self.date = date
        self.type = p_type # When in use, expired and used.
