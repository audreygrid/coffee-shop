import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_coffee_attributes(self):
        coffee = Coffee("Latte", 3.5)
        self.assertEqual(coffee.name, "Latte")
        self.assertEqual(coffee.price, 3.5)

if __name__ == '__main__':
    unittest.main()
