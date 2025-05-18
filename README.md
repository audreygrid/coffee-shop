Coffee Shop Challenge
This is a simple Python OOP project modeling a coffee shop setup. It’s got three main classes: Customer, Coffee, and Order. The goal is to handle relationships between them and support some basic data tracking like how many times a coffee was ordered, who ordered what, and so on.

Models
Customer
Init with a name (string, 1–15 chars)

.name property — getter/setter with type/length validation

.orders() — returns all their orders

.coffees() — returns unique list of coffees they've ordered

.create_order(coffee, price) — shortcut to create a new order

Coffee
Init with a name (string, min 3 chars)

.name is read-only after init

.orders() — returns all orders for this coffee

.customers() — returns unique list of customers who ordered it

.num_orders() — count of orders for this coffee

.average_price() — avg price across all orders

Order
Init with a Customer, Coffee, and price (float between 1.0–10.0)

.customer, .coffee, .price are all read-only

Bonus
Customer.most_aficionado(coffee) — class method that returns the customer who spent the most on a specific coffee (or None if no orders)

Quick Example
python
Copy
Edit
c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")

c1.create_order(latte, 4.5)
c2.create_order(latte, 5.0)

print(latte.num_orders())           # 2
print(latte.average_price())        # 4.75
print(Customer.most_aficionado(latte).name)  # Bob
Notes
All data is in memory — no DB or file saving

No external packages


Type checks and validations are in place so things break early if we mess something up
