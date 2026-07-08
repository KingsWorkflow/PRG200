# Goodie Bag Tracker

bag_cost = float(input("Enter fixed cost per goodie bag: Rs. "))
total_favors = int(input("Enter total favor inventory (starting stock): "))

favors_used = 0

while True:
    response = input("Hand out a bag? (yes/no): ").lower()

    if response == "no":
        break

    if favors_used >= total_favors:
        print("Out of favors! Cannot hand out more bags.")
        break

    favors_used += 1
    print(f"Bag #{favors_used} handed out.")

# After the loop terminates, calculate final values
total_expenditure = favors_used * bag_cost
remaining_favors = total_favors - favors_used

print("\n----- Final Summary -----")
print(f"Total bags handed out: {favors_used}")
print(f"a) Total expenditure on goodie bags: Rs. {total_expenditure:.2f}")
print(f"b) Remaining favor inventory: {remaining_favors}")