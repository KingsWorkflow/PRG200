# NEA Electricity Bill Calculator
previous_reading = float(input("Enter previous meter reading (kWh): "))
current_reading = float(input("Enter current meter reading (kWh): "))
rate_per_unit = float(input("Enter rate per unit (Rs/kWh): "))
service_charge = float(input("Enter fixed monthly service charge (Rs): "))

units_consumed = current_reading - previous_reading
energy_cost = units_consumed * rate_per_unit
total_bill = energy_cost + service_charge

print(f"\n--- Electricity Bill Summary ---")
print(f"Units consumed: {units_consumed:.2f} kWh")
print(f"Energy cost: Rs. {energy_cost:.2f}")
print(f"Service charge: Rs. {service_charge:.2f}")
print(f"Total bill: Rs. {total_bill:.2f}")