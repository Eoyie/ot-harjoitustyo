#from respositories.expire_repository import (expire_repository as default_expire_repository)    En vielä osaa

class Expire:
    def __init__(self):
        self.exp_repository = []        # Tässä vaiheessa toteutan vain listalla, koska en vielä osaa repositery osuutta!!
    
    #def check_product_in_list(self, product):

    def add_product(self, product):
        # Tämä vain auttaa muistamaan mikä mikäkin kohta ei siis oikeasti osa add_productia

        self.expire_id = product[0]          # vielä manuaalinen, mutta muutetaan
        self.expire_name = product[1]
        self.expire_type = product[2]        # Tähän varmaan esim. 0:jääkaappi 1:pakastin 2:kaappi
        self.expire_date = product[3]
        self.expire_status = product[4]      # Olkoon 0 ei käytettävissä ja 1 vanha

        self.exp_repository.append(product)

    def delete_product(self, product):
                                        # Tuleva ongelma, jos on kaksi saman nimistä!!! Ehkä UI käyttö hoitaa ongelman? Tämä vielä manuaalinen!!
        for exp in self.exp_repository:
            if exp[1] == product:
                self.exp_repository.remove(exp)

    def delete_all(self):

        self.exp_repository = []

    def spoiled_product(self, product): # Manuaalinen valinta

        for exp in self.exp_repository:
            if exp[1] == product:
                exp[4] = 1
    
    #def check_all_status(self):          Mahd. osa listan hakua, jossa automaattisesti vaihdettaisiin oikeassa ajassa kaikki statuset jos vanhoja 

    #def get_spoiled_product_list(self):
        
    #    self.check_status()
    #    for exp in self.exp_repository:
    #        if exp[]