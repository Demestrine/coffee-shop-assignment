
from customer import Customer
from coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price: float):
        if not isinstance(customer, Customer):
            raise Exception("Invalid Customer object")
        if not isinstance(coffee, Coffee):
            raise Exception("Invalid Coffee object")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise Exception("Price must be a float between 1.0 and 10.0")

        self._price = float(price)
        self.customer = customer
        self.coffee = coffee
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price
