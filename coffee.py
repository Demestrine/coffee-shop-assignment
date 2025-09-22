
from order import Order

class Coffee:
    all_coffees = []

    def __init__(self, name: str):
        self._name = None
        self.name = name  # setter validation
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            raise Exception("Coffee name cannot be changed once set")
        if not isinstance(value, str) or len(value) < 3:
            raise Exception("Coffee name must be a string with at least 3 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders_list = self.orders()
        if not orders_list:
            return 0
        return sum(order.price for order in orders_list) / len(orders_list)

