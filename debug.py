from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create some orders
order1 = Order(alice, latte, 5.0)
order2 = Order(bob, espresso, 4.0)
order3 = Order(alice, espresso, 6.0)

# Print customers
print(alice)        # Customer('Alice')
print(bob)          # Customer('Bob')

# Print coffees
print(latte)        # Coffee('Latte')
print(espresso)     # Coffee('Espresso')

# Print orders
print(order1)       # Order(Alice, Latte, 5.0)
print(order2)       # Order(Bob, Espresso, 4.0)
print(order3)       # Order(Alice, Espresso, 6.0)

# Print orders that Alice made
print("Alice's orders:", alice.orders())

# Print coffees Alice ordered
print("Alice's coffees:", alice.coffees())

# Print customers who ordered Latte
print("Latte customers:", latte.customers())

# Print number of orders for Espresso
print("Espresso number of orders:", espresso.num_orders())

# Print average price for Espresso
print("Espresso average price:", espresso.average_price())
