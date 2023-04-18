from pathlib import Path
from entities.exp import Exp
from config import EXP_FILE_PATH

class ExpRepository:
    def __init__(self,file_path):
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()

    def find_all(self):
        return self.read()

    def read(self):
        products = []
        self.ensure_file_exists()

        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                part = row.split(";")

                exp_id = part[0]
                product = part[1]
                #type = part[2]
                #date = part[3]
                expired = part[2] = "1"
                #username = part[5]

                #user = user_repository.find_by_username(username) if username else None

                products.append(Exp(product, expired, exp_id))

        return products

    def read2(self):
        products = []
        self.ensure_file_exists()

        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                part = row.split(";")

                exp_id = part[0]
                product = part[1]
                #type = part[2]
                #date = part[3]
                expired = part[2] = "1"

                products.append((product, expired, exp_id))

        return products

    def create(self, product):

        products = self.find_all()

        products.append(product)

        self.write(products)

        return product

    def write(self, products):
        self.ensure_file_exists()

        with open(self.file_path, "w", encoding="utf-8") as file:
            for product in products:
                #exp_string = "1" if product.expired else "0"
                row = f"{product.id};{product.product};{product.expired}"

                file.write(row+"\n")

    def set_expired(self, exp_id, expired = True):
        products = self.find_all()
        for product in products:
            if product.id == exp_id:
                product.expired = expired

        self.write(products)

    def delete_product(self, product_num):
        products = self.find_all()
        products_left = []

        # Tulee muuttumaan. Väliaikainen ratkaisu :)
        for i in range(len(products)):
            if i != product_num:
                products_left.append(products[i])

        self.write(products_left)

    def delete_all(self):
        self.write([])

exp_repository = ExpRepository(EXP_FILE_PATH)
