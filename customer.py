# This file handles everything about our customers  like creating profiles, tracking their orders, and finding out who likes what coffee

class Customer:
# We keep a list of all customers so we can track them globally
    all_customers = []
    
    def __init__(self, name):
# When a new customer signs up, we need to validate their name
# Using a private variable with a property gives us control
        self._name = None
        self.name = name  # This uses the setter below for validation
        Customer.all_customers.append(self)  # Add to our master list
    
    @property
    def name(self):
# Simple getter - just return the stored name
        return self._name
    
    @name.setter
    def name(self, value):
# We need to make sure names are valid
# No numbers, not too short, not too long
        if not isinstance(value, str):
            raise Exception("Customer names should be text, not numbers")
        if not 1 <= len(value) <= 15:
            raise Exception("Names need to be 1-15 characters")
        self._name = value
    
    def orders(self):
# Find all orders this customer has made
# We import here to avoid circular import issues
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
 # Get all unique coffees this customer has tried
# Using set() to avoid duplicates if they ordered same coffee multiple times
        coffee_list = [order.coffee for order in self.orders()]
        return list(set(coffee_list))
    
    def create_order(self, coffee, price):
# Convenience method to create an order for this customer
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
# Find which customer spends the most on a particular coffee
# Useful for loyalty programs or special offers
        
# If no one ordered this coffee yet, return None
        if not coffee.orders():
            return None
        
# Track how much each customer spent on this coffee
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        
# Find the customer with the highest spending
        return max(customer_spending, key=customer_spending.get)