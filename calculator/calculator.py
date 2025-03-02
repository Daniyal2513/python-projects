def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error: Division by zero."
    else:
        return x/y
    
def calculator():
    while True:
        print("=====BASIC CALCULATOR=====")
        print("1. Add (+)")
        print("2. Suctract (-)")
        print("3. Multiply (x)")
        print("4. Divide (/) ")
        print("5. Exit")

        choice = input("Enter choice:")
        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter num1:"))
                num2 = float(input("Enter num2:"))

                if choice == "1":
                    print(f"Result:{num1} + {num2} = {add(num1,num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1,num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1,num2)}")
                elif choice == "4":
                    print(f"Result: {num1} / {num2} = {divide(num1,num2)}")
            except ValueError:
                print("Invalid input! enter numberic value")
        
        else:
            print("Invalid choice.Try again!")

calculator()
