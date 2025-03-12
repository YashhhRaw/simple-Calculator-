def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y !=0:
        return x / y
    else:
        return "Error: Division by zero"
    
def simple_calc():
    print("Select operation you want to do:")
    print("1. Addition")
    print("2. subraction")
    print("3. Multiplication")
    print("4. Division")
    print("Chooose the operation:")
    
    while True:
        operation = input("Enter the operation Number:")
        if operation in ("1", "2", "3", "4"):
            num1 = int(input("Enter the first number:"))
            num2 = int(input("Enter the second number:"))
        if operation == "1":
            print(add(num1, num2))
        elif operation == "2":
            print(sub(num1, num2))
        elif operation == "3":
            print(mul(num1, num2))
        elif operation == "4":
            print(div(num1, num2))
        else:
            print("Invalid number")
        
        next_calc =  input("Do you want to continue the operaition : Yes or No :")
        if next_calc.lower() == "no":
            break
        else:
            print()
simple_calc()