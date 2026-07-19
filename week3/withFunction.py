# $5 $50 $500 convert to nepali currency

def convert_to_nepali(amount):
    dollar_rate = 153
    return amount * dollar_rate

dollar_amt=float(input("Enter amount in dollar: "))
print(f"${dollar_amt} is equal to Rs.{convert_to_nepali(dollar_amt)}")

