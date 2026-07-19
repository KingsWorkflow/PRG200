# Taxi Fare Calculator
trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]
 
BASE_FARE = 150       # first 2 km
MID_RATE = 35         # km 3-10
FAR_RATE = 28         # beyond 10 km
NIGHT_SURCHARGE = 0.10  # 10 PM - 5 AM
 
for trip in trips:
    distance = trip["distance"]
    hour = trip["hour"]
 
    if distance <= 2:
        fare = BASE_FARE
    else:
        fare = BASE_FARE
        remaining = distance - 2
        if remaining <= 8:
            fare += remaining * MID_RATE
        else:
            fare += 8 * MID_RATE
            fare += (remaining - 8) * FAR_RATE
 
    is_night = hour >= 22 or hour < 5
    if is_night:
        fare *= (1 + NIGHT_SURCHARGE)
 
    print(f"Distance: {distance} km, Hour: {hour}:00 "
          f"({'Night' if is_night else 'Day'}) -> Fare: NPR {fare:.2f}")
