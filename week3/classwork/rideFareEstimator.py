# Ride Fare Estimator
# Assumed base fare + per-km rate by vehicle type
def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type.lower() == "bike":
        base_fare = 30
        rate_per_km = 12
    elif vehicle_type.lower() == "car":
        base_fare = 100
        rate_per_km = 25
    else:
        print("Invalid vehicle type.")
        return 0
 
    fare = (base_fare + distance_km * rate_per_km) * surge
    return fare
 
print(f"Bike, 8km, no surge: NPR {estimate_fare(8, 'bike'):.2f}")
print(f"Car, 8km, 1.5x surge: NPR {estimate_fare(8, 'car', surge=1.5):.2f}")
