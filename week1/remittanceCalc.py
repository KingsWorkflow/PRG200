# Remittance Calculator
qatar_amount = float(input("Enter amount in qatar: "))
exchange_rate = float(input("Enter current exchange rate (qatar to NPR): "))
fee_percentage = float(input("Enter service fee percentage: "))

fee = qatar_amount * (fee_percentage / 100)
amount_after_fee = qatar_amount - fee
npr_amount = amount_after_fee * exchange_rate

print(f"\n--- Remittance Summary ---")
print(f"Amount sent: {qatar_amount:.2f}")
print(f"Fee charged: {fee:.2f}")
print(f"Amount after fee: {amount_after_fee:.2f}")
print(f"Amount received in NPR: Rs. {npr_amount:.2f}")
