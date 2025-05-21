from coffee import Coffee
from customer import Customer

class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee

    def summary(self):
        return f"{self.customer.name} ordered a {self.coffee.name} for ${self.coffee.price:.2f}"
