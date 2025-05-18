class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name  
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        from order import Order
        matching_orders = []
        for order in Order.all_orders:
            if order.coffee == self:
                matching_orders.append(order)
        return matching_orders

    def customers(self):
        unique_customers = set()
        for order in self.orders():
            unique_customers.add(order.customer)
        return list(unique_customers)

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        all_orders = self.orders()
        if not all_orders:
            return 0.0
        total_price = sum(order.price for order in all_orders)
        return total_price / len(all_orders)

    def __repr__(self):
        return f"Coffee('{self.name}')"



