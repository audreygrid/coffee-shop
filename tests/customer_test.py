import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_customer_name(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

if __name__ == '__main__':
    unittest.main()
