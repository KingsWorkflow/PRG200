# Online Store Discount System
total_purchase = float(input("Enter total purchase amount (NPR): "))
is_loyalty = input("Are you a loyalty member? (yes/no): ").strip().lower() == "yes"
 
if total_purchase < 1000:
    discount_rate = 0
elif total_purchase < 5000:
    discount_rate = 0.05
elif total_purchase < 15000:
    discount_rate = 0.10
else:
    discount_rate = 0.20
 
amount_after_discount = total_purchase * (1 - discount_rate)
 
if is_loyalty:
    amount_after_discount = amount_after_discount * (1 - 0.05)
 
print(f"\n--- Order Summary ---")
print(f"Total purchase: Rs. {total_purchase:.2f}")
print(f"Discount applied: {discount_rate * 100:.0f}%")
print(f"Loyalty member: {'Yes' if is_loyalty else 'No'}")
print(f"Final payable amount: Rs. {amount_after_discount:.2f}")
