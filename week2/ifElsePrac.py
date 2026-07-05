# if 20>10:
#     print("20 is greater than 10")
# else:
#     print("20 is not greater than
# grade slab
marks=[]
stuName=[]
for i in range(20):
    name=input("Enter your name:\n")
    stuName.append(name)
    mark=float(input("Enter your grade: \n"))
    marks.append(mark)
for m in marks:
    for i,val in enumerate(stuName):
        if marks[i]>=90:
            print(f"{val} got Distinction")
        elif  marks[i]>=75:
            print(f"{val} got First Division")
        elif marks[i]>=60:
            print(f"{val} got Second Division")
        elif  marks[i]>=35:
            print(f"{val} got Third Division")
        else:
            print(f"{val} is")
            print("Fail")