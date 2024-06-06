import sqlite3

CONN = sqlite3.connect('coffee_shop.db')
CURSOR = CONN.cursor()

class Coffee:
    def __init__(self, name):
        self.id = None
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (not hasattr(self, 'name')) and (type(name) == str) and (len(name) >= 3):
            self._name = name
        else:
            raise ValueError("Name must be a string of at least 3 characters. Unable to change name once set.")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        cust_set = set([order.customer for order in Order.all if order.coffee == self])
        
        return list(cust_set)
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total = 0
        amount = 0
        for order in self.orders():
            amount += order.price
            total += 1
        return amount / total

class Customer:
    def __init__(self, name):
        self.id = None
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters long.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        coffee_set = set([order.coffee for order in Order.all if order.customer == self])

        return list(coffee_set)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (not hasattr(self, "price")) and (type(price) == float) and (1.0 <= price <= 10.0):
            self._price = price
        else:
            raise ValueError("Price cannot be changed once set")