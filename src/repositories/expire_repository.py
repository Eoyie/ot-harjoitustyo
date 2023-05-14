import os
from pathlib import Path
from datetime import datetime
from entities.exp import Exp
from config import MAIN_FILE_PATH, EXP_FILENAME


class ExpRepository:
    """Tuotteisiin liittyvistä tietokantaoperaatioista vastaava luokka."""

    def __init__(self, def_file_path):
        """Luokan konstruktori.
        Args:
            file_path: Polku tiedostoon, johon tehtävät tallennetaan.
        """
        self.def_file_path = def_file_path
        self.file_path = None

    def update_file_path(self, username):
        """Päivittää reitin käyttäjän tiedostoon."""
        self.file_path = os.path.join(self.def_file_path, username, EXP_FILENAME)

    def ensure_file_exists(self):
        """Varmistaa käyttäjän tiedoston olemassa olon."""
        Path(self.file_path).touch()

    def find_one(self, p_id):
        """Löytää halutun tuotteen.
        
        Returns:
                Haluttu tuote Exp-oliona."""
        products = self.find_all()

        for product in products:
            if product.id == p_id:
                return product
        return False

    def find_all(self):
        """Välittäjä, joka palauttaa readin listan.
        
        Returns:
                Kaikki tuotteet Exp-oliona listassa."""
        return self.read()

    def read(self):
        """Lukee tuotteet tietokannasta ja muuttaa ne listaksi.
        
        Returns:
                Kaikki tuotteet Exp-oliona listassa."""
        products = []
        self.ensure_file_exists()

        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                part = row.split(";")

                p_id = part[0]
                product = part[1]
                date = part[2]
                qty = part[3]
                p_type = part[4]
                products.append(Exp(product, date, qty, p_type, p_id))

        products.sort(key=lambda x: datetime.strptime(x.date,'%d-%m-%Y'))
        return products

    def write(self, products):
        """Kirjoittaa tuotteen/tuotteet CVS-tiedostoon.
        
        Args:
            products: Lista kaikista tuotteista."""
        self.ensure_file_exists()

        with open(self.file_path, "w", encoding="utf-8") as file:
            for product in products:
                row = f"{product.id};{product.product};{product.date};{product.qty};{product.type}"

                file.write(row+"\n")

    def create(self, product):
        """Lisää tuotteen tietokantaan
        
        Args:
            product: Tallenettava tuote Exp-oliona.
        Returns:
            Tallennettu tuote Exp-oliona."""

        products = self.find_all()

        products.append(product)

        self.write(products)

        return product

    def update(self, product, old_p_id):
        """Päivittää yhden tuotteen tiedot.
        
        Args:
            product: Tallennettava tuote Exp-oliona.
            old_p_id: Merkkijonoarvo, joka on päivitettävän tuotteen vanha id."""

        products = self.find_all()
        new_products = []
        for old_product in products:
            if old_p_id == old_product.id:
                new_products.append(product)
            else:
                new_products.append(old_product)
        self.write(new_products)

    def set_expired(self, p_id, p_qty):
        """Asettaa tuotteen vanhentuneeksi.

        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
            p_qty: Merkkijonoarvo, joka kuinka suuri osa tuotteesta muutetaan"""

        return self.set_stage(p_id,3,p_qty)

    def set_used(self, p_id, p_qty):
        """Asettaa tuotteen käytetyksi.

        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id
            p_qty: Merkkijonoarvo, joka kuinka suuri osa tuotteesta muutetaan."""

        self.set_stage(p_id,4,p_qty)

    def set_stage(self, p_id, stage, p_qty):
        """Muuttaa tuotteen tilan.

        Args:
            p_id: Merkkijonoarvo, joka on muutettavan tuotteen id.
            stage: Integralarvo, joka on tila mihin tuote muutetaan
            p_qty: Merkkijonoarvo, joka kuinka suuri osa tuotteesta muutetaan."""
        products = self.find_all()

        for product in products:
            if product.id == p_id:
                stage_id = product.id + str(stage)
                already_id = self.second_check(products,stage_id,p_qty)
                already_product = product
                break

        if not already_id:

            already_product.qty = int(already_product.qty) - int(p_qty)
            if already_product.qty == 0:
                already_product.qty = p_qty
                already_product.type = stage
                self.write(products) 
                return

            product_copy = Exp(already_product.product, already_product.date,
                               p_qty, stage, stage_id)
            products_copy = list(products)
            products_copy.append(product_copy)
            self.write(products_copy)
            return

        for product in products:
            if product.id == p_id:
                product.qty = int(product.qty) - int(p_qty)
                self.write(products)
                return

    def second_check(self,products,stage_id,p_qty):
        """Apu funktio pylintin sääntöjen vuoksi. 
        Tarkistaa onko muutettu tuote jo olemssa."""
        for product_2 in products:
            if product_2.id == stage_id:
                product_2.qty = int(product_2.qty) + int(p_qty)
                self.write(products)
                return True
        return False

    def delete_product(self, p_id):
        """Poistaa tuotteen.
        
        Args:
            p_id: Tuotteen id."""
        products = self.find_all()
        products_left = []

        for product in products:
            if product.id != p_id:
                products_left.append(product)

        self.write(products_left)

    def delete_all(self):
        """Poistaa kaikki tuotteet."""
        self.write([])

    def automatic_expire(self):
        """Päivittää tuotteiden vanhentumiset päivämäärän mukaan.
        
        Returns:
            Päivitetyt tuotteet listassa Exp-oliona."""
        self.ensure_file_exists()
        today = datetime.today().strftime('%d-%m-%Y')

        products = self.find_all()
        check_same_id = {}
        check_help = {}
        for product in products:
            if product.id[-1] == "3":
                check_same_id[product.id[:len(product.id)-1]] = product.id[-1]
                check_help[product.id] = int(product.qty)

        del_products = []
        for product in products:
            if product.date < today and product.type != "4":
                if product.id in check_same_id:
                    stage = check_same_id[product.id]
                    del_product_id = product.id+str(stage)
                    product.qty = int(product.qty) + int(check_help[del_product_id])
                    del_products.append(del_product_id)
                product.type = 3

        self.write(products)
        return del_products


exp_repository = ExpRepository(MAIN_FILE_PATH)
