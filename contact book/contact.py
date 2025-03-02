import json
import os

file_name = "contact.json"

def load_contact():
    if os.path.exists(file_name):
        with open(file_name,"r")as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return{}
    return{}

def save_contact(contact_book):
    with open(file_name,"w") as file:
        json.dump(contact_book,file,indent =4)

def add_contact(phone_num,name,email):
    contact_book = load_contact()
    contact_book[name]={"phone No":phone_num,"Email":email}
    save_contact(contact_book)
    print(f"contact number of {name} added successfully")

def view_contact(name):
    contact_book = load_contact()
    if name in contact_book:
        print(f"name:{name}")
        print(f"phone No:{contact_book[name]['phone No']}")
        print(f"Email:{contact_book[name]['Email']}")
    else:
        print(f"No contact number saved for {name}")

def update_contact(name,new_number):
    contact_book = load_contact()
    if name in contact_book:
        contact_book[name]['phone No'] = new_number
        save_contact(contact_book)
        print(f"Number of {name} updated successfully.")
    else:
        print("No name found")

def delete_contact(name):
    contact_book = load_contact()
    if name in contact_book:
        del contact_book[name]
        save_contact(contact_book)
        print(f"Number of {name} deleted successfully.")
    else:
        print("No name found")

def main():
    contact_book = load_contact()

    while True:
        print("=====Contact Book=====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact No")
        print("4. Delete contact")
        print("5. Exit.")
        choice = input("Enter your choice:")

        if choice == "1":
            name = input("Enter name:")
            phone_num = int(input("Enter number:"))
            email = input("Enter email:")
            add_contact(phone_num,name,email)
        elif choice == "2":
            name = input("Enter name:")
            view_contact(name)
        elif choice == "3":
            name = input("Enter name:")
            new_number = int(input("Enter new number:"))
            update_contact(name,new_number)
        elif choice == "4":
            name = input("Enter name:")
            delete_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()