# Mobile Data Pack Recharge
# Assumed Ncell pack rates
def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 39
    elif gb == 2:
        price = 69
    elif gb == 5:
        price = 149
    elif gb == 10:
        price = 279
    elif gb == 20:
        price = 499
    else:
        print("Pack not available.")
        return None
    return price
 
 
# Test calls
cost1 = recharge_cost(5)
print(f"5GB pack (default validity): NPR {cost1} for 30 days")
 
cost2 = recharge_cost(10, validity_days=45)
print(f"10GB pack (custom validity): NPR {cost2} for 45 days")
