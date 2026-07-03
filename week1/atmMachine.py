pin = "1111"
money = 5000

for i in range(3):
    user_pin = input("Enter PIN: ")
    
    if user_pin == pin:
        print("Welcome!")
        
        while True:
            print("\n1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            
            option = input("Select: ")
            
            if option == "1":
                print("Your balance:", money)
                
            elif option == "2":
                take = float(input("How much: "))
                if take <= money:
                    money = money - take
                    print("Left:", money)
                else:
                    print("Insufficient balance")
                    
            elif option == "3":
                add = float(input("How much: "))
                money = money + add
                print("New balance:", money)
                
            elif option == "4":
                print("Goodbye!")
                break
                
            else:
                print("Wrong choice!")
        break
        
    else:
        print("Wrong PIN!")
        if i == 2:
            print("Card blocked!")