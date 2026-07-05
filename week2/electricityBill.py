storeName=[]
meterUnit=[]

numberOfStore=int(input("Enter number of stores:"))

for i in range(numberOfStore+1):
    stName=input("Enter name of store:")
    storeName.append(stName)
    unit=float(input("Enter unit consumed: "))
    meterUnit.append(unit)

for i,val in enumerate(storeName):
        ut=meterUnit[i]
        if ut<=50:
            billAmt=ut*20
            print(f"Total Bill Amount for {val} is Rs.{billAmt}")
        elif ut>50 and ut<=100:
            billAmt=ut*40
            print(f"Total Bill Amount for {val} is Rs.{billAmt}")
        else:
            billAmt=ut*60
            print(f"Total Bill Amount for {val} is Rs.{billAmt}")

