# Quick test file to make sure everything works together
from customer import Customer
from coffee import Coffee
from order import Order

def debug():
    print("Testing the coffee shop system...")
    print("=" * 40)
    
# Create some test customers
    print("Creating customers...")
    demestrine = Customer("demestrine")
    awuor = Customer("awuor")
    print(f"Made customers: {demestrine.name}, {awuor.name}")
    
# Create coffee menu items
    print("\nCreating coffees...")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    print(f"Menu: {espresso.name}, {latte.name}, {cappuccino.name}")
    
# Place some orders
    print("\nPlacing orders...")
    order1 = Order(demestrine, espresso, 5.0)
    order2 = Order(demestrine, latte, 6.5)
    order3 = Order(awuor, espresso, 5.0)
    order4 = Order(awuor, cappuccino, 7.0)
    print("Orders placed successfully")
    
# Test relationships
    print(f"\nDemestrine ordered {len(demestrine.orders())} times")
    print(f"Demestrine's coffees: {[c.name for c in demestrine.coffees()]}")
    print(f"Espresso customers: {[c.name for c in espresso.customers()]}")
    
# Test analytics
    print(f"\nEspresso stats: {espresso.num_orders()} orders, avg ${espresso.average_price():.2f}")
    
# Test most_aficionado
    big_fan = Customer.most_aficionado(espresso)
    if big_fan:
        print(f"Biggest espresso fan: {big_fan.name}")
    
# Test error handling
    print("\nTesting error cases...")
    try:
        bad_customer = Customer("")
    except Exception as e:
        print(f"Caught error: {e}")
    
    try:
        bad_coffee = Coffee("ab")
    except Exception as e:
        print(f"Caught error: {e}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    debug()