print("---SIMPLE CALCULATOR---")
print("Select an operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    operation = int(input("Enter Choice(1/2/3/4/5): "))
    num1=float(input("Enter num1: "))
    num2=float(input("Enter num2: "))

    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    elif operation==5:
        break
    else:
        print("Invalid Option! Try again")
