# Movie Ticket Price Calculator
# Assumed QFX rates: Regular = NPR 350, Recliner = NPR 600
def ticket_price(seat_type, count):
    if seat_type.lower() == "regular":
        price_per_seat = 350
    elif seat_type.lower() == "recliner":
        price_per_seat = 600
    else:
        print("Invalid seat type.")
        return 0
    return price_per_seat * count
 
print(f"3 Regular tickets: NPR {ticket_price('regular', 3)}")
print(f"2 Recliner tickets: NPR {ticket_price('recliner', 2)}")
