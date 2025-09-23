# Tests for the Coffee class

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    
    def test_coffee_creation(self):
# Basic coffee creation test
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"
    
    def test_invalid_name_length(self):
# Test short coffee names are rejected
        with pytest.raises(Exception):
            Coffee("ab")
    
    def test_name_immutability(self):
# Test that coffee names can't be changed
        coffee = Coffee("Latte")
        with pytest.raises(Exception):
            coffee.name = "NewName"
    
    def test_customers_relationship(self):
# Test finding customers for a coffee
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 6.0)
        
        assert len(coffee.customers()) == 2
        assert customer1 in coffee.customers()
        assert customer2 in coffee.customers()
    
    def test_num_orders(self):
# Test order counting
        coffee = Coffee("Latte")
        customer = Customer("Charlie")
        
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 6.0)
        
        assert coffee.num_orders() == 2
    
    def test_average_price(self):
# Test average price calculation
        coffee = Coffee("Espresso")
        customer = Customer("David")
        
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        
        assert coffee.average_price() == 5.0
    
    def test_average_price_no_orders(self):
# Test average price with no orders
        coffee = Coffee("Americano")
        assert coffee.average_price() == 0