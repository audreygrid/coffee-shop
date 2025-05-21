#/usr/bin/env python3
# class Customer:
#     all_customers = []

#     def __init__(self, name):
#         self.name = name
#         Customer.all_customers.append(self)

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if isinstance(value, str) and 1 <= len(value) <= 15:
#             self._name = value
#         else:
#             raise ValueError("Customer name must be a string between 1 and 15 characters.")

#     def orders(self):
#         return [order for order in Order.all_orders if order.customer == self]

#     def coffees(self):
#         return list({order.coffee for order in self.orders()})

#     def create_order(self, coffee, price):
#         return Order(self, coffee, price)

#     @classmethod
#     def most_aficionado(cls, coffee):
#         customer_spending = {}
#         for order in Order.all_orders:
#             if order.coffee == coffee:
#                 customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
#         if not customer_spending:
#             return None
#         return max(customer_spending, key=customer_spending.get)


# class Coffee:
#     all_coffees = []

#     def __init__(self, name):
#         if isinstance(name, str) and len(name) >= 3:
#             self._name = name
#             Coffee.all_coffees.append(self)
#         else:
#             raise ValueError("Coffee name must be a string of at least 3 characters.")

#     @property
#     def name(self):
#         return self._name  

#     def orders(self):
#         return [order for order in Order.all_orders if order.coffee == self]

#     def customers(self):
#         return list({order.customer for order in self.orders()})

#     def num_orders(self):
#         return len(self.orders())

#     def average_price(self):
#         prices = [order.price for order in self.orders()]
#         if not prices:
#             return 0
#         return sum(prices) / len(prices)


# class Order:
#     all_orders = []

#     def __init__(self, customer, coffee, price):
#         if not isinstance(customer, Customer):
#             raise TypeError("customer must be an instance of Customer")
#         if not isinstance(coffee, Coffee):
#             raise TypeError("coffee must be an instance of Coffee")
#         if not isinstance(price, float) or not (1.0 <= price <= 10.0):
#             raise ValueError("price must be a float between 1.0 and 10.0")

#         self._customer = customer
#         self._coffee = coffee
#         self._price = price
#         Order.all_orders.append(self)

#     @property
#     def customer(self):
#         return self._customer

#     @property
#     def coffee(self):
#         return self._coffee

#     @property
#     def price(self):
#         return self._price  

# c1 = Customer("Alice")
# c2 = Customer("Bob")
# c3 = Customer("Charlie")

# coffee1 = Coffee("Latte")
# coffee2 = Coffee("Espresso")

# c1.create_order(coffee1, 3.5)
# c1.create_order(coffee2, 2.5)
# c2.create_order(coffee1, 5.0)
# c2.create_order(coffee1, 4.0)
# c3.create_order(coffee1, 3.0)

# print(coffee1.num_orders())          
# print(coffee1.average_price())      
# print([coffee.name for coffee in c1.coffees()])           
# print(Coffee("Mocha").customers())   
# print(Customer.most_aficionado(coffee1).name)  
