# Small Shop Billing and Inventory System
def process_order(inventory, cart):
    grand_total = 0
    print("---- Bill ----")
    purchased_items = []
 
    for item, qty in cart.items():
        if item in inventory and inventory[item]["stock"] >= qty:
            price = inventory[item]["price"]
            item_total = price * qty
            grand_total += item_total
            inventory[item]["stock"] -= qty
            purchased_items.append(item)
            print(f"{item} x{qty} = NPR {item_total}")
        else:
            print(f"Sorry, not enough stock for {item}")
 
    print("--------------")
    print(f"Grand Total: NPR {grand_total}")
 
    stock_str = ", ".join(
        f"{item}={inventory[item]['stock']}" for item in purchased_items
    )
    print(f"Updated stock: {stock_str}")
 
 
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30},
}
cart = {"rice": 2, "milk": 3, "eggs": 12}
 
process_order(inventory, cart)
