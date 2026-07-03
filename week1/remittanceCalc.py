# Remittance Calculator
usd_amount = float(input("Enter amount in USD: "))
exchange_rate = float(input("Enter current exchange rate (USD to NPR): "))
fee_percentage = float(input("Enter service fee percentage: "))

fee = usd_amount * (fee_percentage / 100)
amount_after_fee = usd_amount - fee
npr_amount = amount_after_fee * exchange_rate

print(f"\n--- Remittance Summary ---")
print(f"Amount sent: ${usd_amount:.2f}")
print(f"Fee charged: ${fee:.2f}")
print(f"Amount after fee: ${amount_after_fee:.2f}")
print(f"Amount received in NPR: Rs. {npr_amount:.2f}")