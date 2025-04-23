#18. Property Decorators
class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage
product = Product()
product.price = 100
print(product.price)
del product.price