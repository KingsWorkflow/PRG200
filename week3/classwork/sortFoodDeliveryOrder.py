# Sorting Food Delivery Orders
orders = [(101, 25), (102, 10), (103, 40), (104, 5)]
 
orders.sort(key=lambda order: order[1])
 
print("Orders sorted by delivery time (soonest first):")
for order_id, delivery_minutes in orders:
    print(f"Order {order_id}: {delivery_minutes} min")
