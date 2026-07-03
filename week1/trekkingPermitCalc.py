# Trekking Permit Cost Calculator
num_trekkers = int(input("Enter number of trekkers: "))
per_person_fee = float(input("Enter per-person TIMS + ACAP fee (Rs): "))
agency_charge_percent = 5  # 5% agency service charge

total_permit_cost = num_trekkers * per_person_fee
agency_charge = total_permit_cost * (agency_charge_percent / 100)
total_cost = total_permit_cost + agency_charge
average_cost = total_cost / num_trekkers

print(f"\n--- Trekking Permit Summary ---")
print(f"Number of trekkers: {num_trekkers}")
print(f"Total permit cost: Rs. {total_permit_cost:.2f}")
print(f"Agency service charge (5%): Rs. {agency_charge:.2f}")
print(f"Total cost for group: Rs. {total_cost:.2f}")
print(f"Average cost per person: Rs. {average_cost:.2f}")