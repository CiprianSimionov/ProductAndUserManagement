"""implementam clasa ProductsRepository
cu metodele definite in interfata RepositoryInterface()
pentru obiectul Product,
(create, read, update si delete)"""
from repository.repository_interface import RepositoryInterface
from products.product import Product


class ProductsRepository(RepositoryInterface):
    def __init__(self):
        self.products = []

    def create(self, data):
        id = len(self.products) + 1
        product = Product(product_id=id, **data)
        self.products.append(product)
        print(f"Product {product.name} has been created")

    def read(self, entry_id):
        produs = None
        for product in self.products:
            if entry_id == product.product_id:
                produs = product
                break
        if produs:
            print(f"The id is: {produs.product_id} \n"
                f"Product name is: {produs.name} \n"
                f"Product price is: {produs.price} \n"
                f"Product quantity is: {produs.quantity}")

        else:
            print(f"The product with id {entry_id} is not available.")


    def update(self, entry_id, new_data):
        produs = None
        for product in self.products:
            if entry_id == product.product_id:
                produs = product
                break
        if produs:
            produs.name = new_data.get("name", produs.name)
            produs.price = new_data.get("price", produs.price)
            produs.quantity = new_data.get("quantity", produs.quantity)
            print(f"The product with id: {produs.product_id} has been updated.")
        else:
            print(f"The product with id: {entry_id} hasn't been found.")

    def delete(self, entry_id):
        produs = None
        for product in self.products:
            if entry_id == product.product_id:
                produs = product
                break
        if produs:
            self.products.remove(produs)
            print(f"The product with id: {entry_id} has been deleted.")
        else:
            print(f"The product with id: {entry_id} hasn't been found.")

