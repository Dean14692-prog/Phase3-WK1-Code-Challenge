class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        from order import Order
        matching_orders = []
        for order in Order.all_orders:
            if order.customer == self:
                matching_orders.append(order)
        return matching_orders

    def coffees(self):
        unique_coffees = set()
        for order in self.orders():
            unique_coffees.add(order.coffee)
        return list(unique_coffees)

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order

customer = Customer("Dennis")
print(f"Welcome {customer.name}, what would you like to order today?")