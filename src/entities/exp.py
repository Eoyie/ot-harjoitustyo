import uuid

class Exp:
    def __init__(self, product, expired=False, exp_id=None):
        self.id = exp_id or str(uuid.uuid4())
        self.product = product
        #self.type = type
        #self.date = date
        self.expired = expired