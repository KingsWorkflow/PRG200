# Automatic Group Expense Tracker
print("=" * 50)
print("   GROUP EXPENSE TRACKER")
print("   Enter expenses and we'll calculate everything!")
print("=" * 50)

members = []
num_members = int(input("\nHow many people in the group? "))

for i in range(num_members):
    name = input(f"Enter name of person {i+1}: ")
    members.append(name)

print(f"\n✅ Group members: {', '.join(members)}")
print("-" * 50)

expenses = {}  # Dictionary to store each person's total expenses

for member in members:
    print(f"\n--- {member}'s Expenses ---")
    total = 0
    
    while True:
        amount = input(f"Enter expense amount (or 'done' to finish): ")
        
        if amount.lower() == "done":
            break
            
        try:
            amount = float(amount)
            if amount < 0:
                print("Amount cannot be negative!")
                continue
            total += amount
            print(f"  ✓ Added Rs.{amount:.2f} | Total so far: Rs.{total:.2f}")
        except ValueError:
            print("Please enter a valid number!")
    
    expenses[member] = total
    print(f"📝 {member}'s total expense: Rs.{total:.2f}")

print("\n" + "=" * 50)
print("   AUTOMATIC CALCULATION")
print("=" * 50)

# Calculate total spending
total_spent = sum(expenses.values())
average_per_person = total_spent / num_members

print(f"\n💰 Total money spent: Rs.{total_spent:.2f}")
print(f"👥 Each person should spend: Rs.{average_per_person:.2f}")
print("-" * 50)

# Show each person's status
print("\n--- PERSONAL SUMMARY ---")
for member in members:
    spent = expenses[member]
    difference = spent - average_per_person
    
    if difference > 0:
        print(f"{member}: Spent Rs.{spent:.2f} | Should GET BACK Rs.{difference:.2f}")
    elif difference < 0:
        print(f"{member}: Spent Rs.{spent:.2f} | Should PAY Rs.{-difference:.2f}")
    else:
        print(f"{member}: Spent Rs.{spent:.2f} | ✅ SETTLED!")

print("\n" + "=" * 50)
print("   WHO PAYS WHOM")
print("=" * 50)

# Create list of who owes and who is owed
owes = []  # People who need to pay
owed = []  # People who should receive money

for member in members:
    spent = expenses[member]
    diff = spent - average_per_person
    if diff < 0:
        owes.append({"name": member, "amount": -diff})
    elif diff > 0:
        owed.append({"name": member, "amount": diff})

# Match who pays whom
if not owes and not owed:
    print("\n✅ Everyone is settled! No payments needed!")
else:
    print("\n--- Payment Instructions ---")
    for payer in owes:
        remaining = payer["amount"]
        print(f"\n{payer['name']} needs to pay Rs.{payer['amount']:.2f}")
        
        for receiver in owed:
            if remaining > 0 and receiver["amount"] > 0:
                payment = min(remaining, receiver["amount"])
                print(f"  → Pay Rs.{payment:.2f} to {receiver['name']}")
                remaining -= payment
                receiver["amount"] -= payment