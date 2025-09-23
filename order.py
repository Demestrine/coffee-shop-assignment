class Order:
# Keep track of every order ever placed
    all_orders = []
    
    def __init__(self, customer, coffee, price):
 # Create a new order linking customer, coffee, and price
        self._price = None
        self.price = price  # Uses setter for validation
        self._customer = customer
        self._coffee = coffee
        Order.all_orders.append(self)  # Add to order history
    
    @property
    def price(self):
 # Get the order price
        return self._price
    
    @price.setter
    def price(self, value):
# Price validation: must be float, between 1-10, and immutable
        if not isinstance(value, float):
            raise Exception("Price should be a decimal number")
        if not 1.0 <= value <= 10.0:
            raise Exception("Price should be between 1.0 and 10.0")
        if self._price is not None:
            raise Exception("Can't change price after order is created")
        self._price = value
    
    @property
    def customer(self):
# Which customer placed this order?
        return self._customer
    
    @property
    def coffee(self):
# Which coffee was ordered?
        return self._coffee