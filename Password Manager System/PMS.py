import hashlib
import json
import os

file_name = "password.json"
def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data,file,indent = 4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(service,username,password):
    data = load_data()
    hash_pw = hash_password(password)
    data[service] = {"username":username, "password":hash_pw}
    save_data(data)
    print(f"Password for {service} added successfully")

def view_password(service):
    data= load_data()
    if service in data:
        print(f"service:{service}")
        print(f"username:{data[service]['username']}")
        print(f"password:{data[service]['password']}")
    else:
        print(f"No password for {service} found")

def update_password(service,new_password):
    data = load_data()
    if service in data:
        data[service]["password"] = hash_password(new_password)
        save_data(data)
        print(f"password for {service} updated successfully")
    else:
        print(f"No service found")

def delete_password(service):
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        print(f"password for {service} deleted successfully")
    else:
        print("No service found")

def main():
    while True:
        print("=====WELCON TO MANAGER SYSTEM=====")
        print("1. Add password")
        print("2. View password")
        print("3. Update password")
        print("4. Delete password")
        print("5. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            service = input("Enter your service:")
            username = input("Enter your username:")
            password = input("Enter your password:")
            add_password(service,username,password)
       
        elif choice == "2":
            service = input("Enter your service:")
            view_password(service)
        elif choice == "3":
            service = input("Enter your service:")
            new_password = input("Enter your password:")
            update_password(service,new_password)
        elif choice == "4":
            service = input("Enter your service:")
            delete_password(service)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()
    