import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_summary(self):
        customer = Customer("Bob")
        coffee = Coffee("Espresso", 2.5)
        order = Order(customer, coffee)
        expected_summary = "Bob ordered a Espresso for $2.50"
        self.assertEqual(order.summary(), expected_summary)

if __name__ == '__main__':
    unittest.main()
