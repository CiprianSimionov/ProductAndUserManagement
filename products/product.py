"""Implementam clasa Product()"""

class Product:
    def __init__(self, product_id, name, price, quantity=1):
        #when setting quantity 1 as param, when no data is inserted,
        #the value by default will be 1
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
