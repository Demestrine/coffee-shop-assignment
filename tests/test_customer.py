import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    """Test suite for all customer-related functionality"""
    
    def test_customer_creation(self):
        """Basic test - can we create a customer with a valid name?"""
        customer = Customer("Awuor")
        assert customer.name == "Awuor"  # Should store the name correctly

    def test_invalid_name_length(self):
        """Test that we properly reject names that are too short or too long"""
# Empty name should be rejected
        with pytest.raises(Exception):
            Customer("")
        
# Really long name should also be rejected
        with pytest.raises(Exception):
            Customer("ThisNameIsWayTooLongForOurSystem")
    
    def test_invalid_name_type(self):
        """Make sure we only accept strings, not numbers or other types"""
        with pytest.raises(Exception):
            Customer(123)  # Numbers aren't valid names!
    
    def test_orders_relationship(self):
        """Test that we can find all orders for a specific customer"""
        customer = Customer("Miminifire")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        
# The order should appear in the customer's order history
        assert order in customer.orders()
        assert len(customer.orders()) == 1
    
    def test_coffees_relationship(self):
        """Test that we get unique coffees a customer has ordered"""
        customer = Customer("Demmy")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        
# Customer orders two different coffees
        Order(customer, coffee1, 5.0)
        Order(customer, coffee2, 6.0)
        
# Should see both coffees in their history
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()
        assert coffee2 in customer.coffees()
    
    def test_create_order(self):
        """Test the convenience method for creating orders"""
        customer = Customer("Wantaaaaam")
        coffee = Coffee("Mocha")
        order = customer.create_order(coffee, 8.5)
        
# The created order should link back to the right customer and coffee
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 8.5