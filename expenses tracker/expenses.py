import json
import os

file_name = "expenses.json"

def read_transaction():
    if os.path.exists(file_name):
        with open(file_name, "r")as file:
            return json.load(file)
        
    return []

def save_transaction(expenses):
    with open(file_name, "w")as file:
        json.dump(expenses,file,indent = 4)

def add_transaction():
    expenses = read_transaction()
    category = input("Enter category (Food,Transport,etc):").capitalize()
    try:
        date = input("Enter date (yyyy-mm-dd):")
        amount  = float(input("Enter amount:"))
        expenses.append({"category":category, "amount":amount, "date":date})
        save_transaction(expenses)
        print("expense add successfully")
    except:
        print("Invalid amount,Please try again.")

def view_transaction():
    expenses = read_transaction()
    if not expenses:
        print("No expense found")
    else:
        print("Expenses:")
        print("{:<15}  {:<30} {:<15}".format("Date","Category","Amount"))
        print("-"*55)
        for exp in expenses:
            print("{:<15}  {:<30} {:<15}".format(exp['date'],exp['category'],exp['amount']))

    print()
            
        # for index,exp in enumerate(expenses,1):
        #     print(f"{index}.{exp['date']},{exp['category']},${exp['amount']:.2f}")
          
def delete_transaction():
    expenses = read_transaction()
    try:
        index = int(input("Enter index number:")) - 1
        if 0 <= index < len(expenses):
            expenses.pop(index)
            save_transaction(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid index, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")

def main():
    while True:
        print("=====Expenses Tracker=====")
        print("1. Add expense")
        print("2. View expense")
        print("3. Delete expense")
        print("4. Exit.")

        choice  = input("Enter your choice:")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transaction()
        elif choice == "3":
            delete_transaction() 
        elif choice == "4":
            print("GoodBye!")
            break
        else:
            print("Invalid choice,Try again!")

if __name__ == "__main__":
    main()
