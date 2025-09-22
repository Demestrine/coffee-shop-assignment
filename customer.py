from order import Order
from coffee import Coffee

class Customer:
    all_customers = []

    def __init__(self, name: str):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise Exception("Customer name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        """Return all orders made by this customer"""
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        """Return a list of unique coffees this customer has purchased"""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        """Create a new order linking this customer to a coffee"""
        if not isinstance(coffee, Coffee):
            raise Exception("Must provide a valid Coffee object")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the customer who spent the most on a specific coffee"""
        if not isinstance(coffee, Coffee):
            raise Exception("Must provide a valid Coffee object")
        max_spent = 0
        top_customer = None
        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                top_customer = customer
        return top_customer
