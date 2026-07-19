# ATM Withdrawal Validator
balance = float(input("Enter current account balance (NPR): "))
daily_withdrawn = float(input("Enter amount already withdrawn today (NPR): "))
amount = float(input("Enter amount to withdraw (NPR): "))
 
DAILY_LIMIT = 50000
 
if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")
elif amount > balance:
    print("Insufficient balance.")
elif daily_withdrawn + amount > DAILY_LIMIT:
    print("Daily withdrawal limit reached.")
else:
    balance -= amount
    daily_withdrawn += amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance:.2f}")
