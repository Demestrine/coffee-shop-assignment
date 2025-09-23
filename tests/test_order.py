# Tests for the Order class

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    
    def test_order_creation(self):
# Basic order creation test
        customer = Customer("wantam")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 7.5)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 7.5
    
    def test_invalid_price_range(self):
 # Test price range validation
        customer = Customer("Mustgo")
        coffee = Coffee("Americano")
        
        with pytest.raises(Exception):
            Order(customer, coffee, 0.5)  # Too low
        
        with pytest.raises(Exception):
            Order(customer, coffee, 15.0)  # Too high
    
    def test_price_immutability(self):
# Test that prices can't be changed
        customer = Customer("Awuor")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        
        with pytest.raises(Exception):
            order.price = 6.0
    
    def test_invalid_price_type(self):
 # Test that non-float prices are rejected
        customer = Customer("Mustmustgooo")
        coffee = Coffee("Espresso")
        
        with pytest.raises(Exception):
            Order(customer, coffee, "5.0")  # String instead of float