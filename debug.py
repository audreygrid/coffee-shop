from customer import Customer
from coffee import Coffee
from order import Order

def main():
    customer = Customer("Charlie")
    coffee = Coffee("Cappuccino", 4.0)
    order = Order(customer, coffee)
    print(order.summary())

if __name__ == '__main__':
    main()
