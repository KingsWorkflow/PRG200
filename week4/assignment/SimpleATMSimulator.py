# Simple ATM Simulator
accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"},
}
 
 
def atm(account_id, pin, action, amount=0):
    if account_id not in accounts:
        print("Account not found")
        return
 
    account = accounts[account_id]
    if account["pin"] != pin:
        print("Incorrect PIN")
        return
 
    if action == "balance":
        print(f"{account['name']}: NPR {account['balance']}")
    elif action == "deposit":
        account["balance"] += amount
        print(f"Deposit successful. New balance: NPR {account['balance']}")
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"Withdrawal successful. New balance: NPR {account['balance']}")
    else:
        print("Invalid action")
 
 
# Test calls
atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)   # wrong PIN
atm("A002", "5678", "deposit",  3000)
atm("A003", "9012", "withdraw", 25000)  # insufficient funds
atm("A004", "1111", "balance")           # account not found
