from pathlib import Path
from datetime import datetime
from entities.exp import Exp
from config import EXP_FILE_PATH

class ExpRepository:
    """Tuotteisiin liittyvistä tietokantaoperaatioista vastaava luokka."""

    def __init__(self,file_path):
        """Luokan konstruktori.
        Args:
            file_path: Polku tiedostoon, johon tehtävät tallennetaan.
        """
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()

    def find_all(self):
        return self.read()

    def read(self):
        """Lukee tuotteet tietokannasta ja muuttaa ne listaksi
        
        Returns:
                Kaikki tuotteet listana"""
        products = []
        self.ensure_file_exists()

        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                part = row.split(";")

                p_id = part[0]
                product = part[1]
                date = part[2]
                p_type = part[3]
                #username = part[5]

                #user = user_repository.find_by_username(username) if username else None
                products.append(Exp(product, date, p_type, p_id))

        products.sort(key=lambda x: datetime.strptime(x.date,'%d-%m-%Y'))
        return products

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

    def write(self, products):
        """Kirjoittaa tuotteen/tuotteet CVS-tiedostoon
        
        Args:
            products: Lista kaikista tuotteista."""
        self.ensure_file_exists()

        with open(self.file_path, "w", encoding="utf-8") as file:
            for product in products:
                row = f"{product.id};{product.product};{product.date};{product.type}"

                file.write(row+"\n")

    def set_expired(self, p_id):
        return self.set_stage(p_id,3)

    def set_used(self, p_id):
        return self.set_stage(p_id,4)

    def set_stage(self,p_id,stage):
        products = self.find_all()
        for product in products:
            if product.id == p_id:
                product.type = stage
                s_product = product
        self.write(products)
        return s_product

    def delete_product(self, exp_id):
        products = self.find_all()
        products_left = []

        for i in products:
            if i.id != exp_id:
                products_left.append(i)

        self.write(products_left)

    def delete_all(self):
        self.write([])

exp_repository = ExpRepository(EXP_FILE_PATH)
