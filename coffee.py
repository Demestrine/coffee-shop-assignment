# This file manages our coffee menu items and their relationships with orders

class Coffee:
# Global list of all coffee types we offer
    all_coffees = []
    
    def __init__(self, name):
# Set up a new coffee menu item
        self._name = None
        self.name = name  # Uses the setter for validation
        Coffee.all_coffees.append(self)  # Add to menu
    
    @property
    def name(self):
# Just return the coffee name
        return self._name
    
    @name.setter
    def name(self, value):
# Coffee names have specific rules:
# Must be string, at least 3 chars, and can't change once set
        if not isinstance(value, str):
            raise Exception("Coffee names should be text")
        if len(value) < 3:
            raise Exception("Coffee names need at least 3 characters")
        if self._name is not None:
            raise Exception("Can't rename coffee after it's created")
        self._name = value
    
    def orders(self):
# Find all orders that include this coffee
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    
    def customers(self):
# Get all unique customers who ordered this coffee
        customer_list = [order.customer for order in self.orders()]
        return list(set(customer_list))
    
    def num_orders(self):
 # How many times was this coffee ordered?
 # Simple count for popularity tracking
        return len(self.orders())
    
    def average_price(self):
 # Calculate the average price paid for this coffee
        orders = self.orders()
        if not orders:
            return 0  # Avoid division by zero
        
        total = sum(order.price for order in orders)
        return total / len(orders)
