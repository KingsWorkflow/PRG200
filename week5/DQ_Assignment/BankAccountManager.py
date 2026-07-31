# Bank Account Manager
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
 
    def get_balance(self):
        print(f"{self.name}: NPR {self.balance}")
 
 
accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]
accounts = [BankAccount(name, acc_num, bal) for name, acc_num, bal in accounts_data]
 
 
def find_account(acc_num):
    for acc in accounts:
        if acc.account_number == acc_num:
            return acc
    return None
 
 
find_account("A002").deposit(3000)
find_account("A003").withdraw(15000)   # insufficient funds
find_account("A001").withdraw(2000)
 
for acc in accounts:
    acc.get_balance()
