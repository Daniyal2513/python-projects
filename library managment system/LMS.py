import os 

file_name = "LMS.txt"

def load_book():
    books = []
    if os.path.exists(file_name):
        with open(file_name, "r")as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:
                 books.append({
                    "ID": parts[0],
                    "Title": parts[1],
                    "Author": parts[2],
                    "year": parts[3],
                    "available": parts[4],
                    "quantity": parts[5]
                })
    return books

def save_book(books):
   with open(file_name, "w") as file:
       for book in books:
           file.write(f"{book['ID']},{book['Title']},{book['Author']},{book['year']},{book['available']},{book['quantity']}\n")

def add_book(books):
    try:
        new_id = input("Enter ID: ")
        new_title = input("Enter Title: ").capitalize()
        author = input("Enter Author: ").capitalize()
        year = input("Enter year: ")
        available = input("Enter available (True/False): ").strip() == "True"       
    except ValueError:
        print("Invalid input")
        return
    
    #check if the id is unique
    # for book in books:
    #     if book["ID"] == new_id:
    #         print("ID already exists")
    #         return  
    # check if the title already exists and update availablitiy count.
    for book in books:
        if book["Title"].lower == new_title.lower() or book["ID"].lower() == new_id.lower():
            book["quantity"] += 1
            save_book(books)
            print("Book quantity updated")
            return
    books.append({
        "ID": new_id,
        "Title": new_title,
        "Author": author,
        "year": year,
        "available": available,
        "quantity": 1
    })
    save_book(books)
    print("Book added successfully")

def view_book(books):
    if not books:
        print("no book available")
    else:
        print("\nLibrary Books")
        print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10}".format("ID", "Title", "Author", "Year", "Available", "Quantity"))
        print("-"*75)
        for book in books:
            print("{:<10} {:<20} {:<20} {:<10} {:<10} {:<10}".format(book["ID"], book["Title"], book["Author"], book["year"], book["available"],book["quantity"]))
    
    print()

def search_book(books):
    keyword = input("Ener keyword:").strip().lower()
    results=[book for book in books if keyword in book["Title"].lower() or keyword in book["Author"].lower()]
    if results:
        for book in results:
            print(book)
        else:
            print("No book found")

def update_book(books):
    try:
        book_id =int(input("Entr book ID:"))   
    except ValueError:
        print("Invalid ID")
        return
    
    for book in books:
        if book["ID"] == book_id:
            print(f"Current record:{book}")
            new_status = input("Enter new availablity (True/False):").strip() == "True"
            book['available']= new_status
            save_book(books)
            print("Book updated successfully")
            return
        else:
            print("No ID found")

def delet_book(books):
    try:
        book_id = int(input("Enter book ID:"))
    except ValueError:
        print("Invalid ID")
        return
    
    for index, book in enumerate(books):
        if book["ID"] == book_id:
            removed = books.pop(index)
            save_book(books)
            print(f"Book removed successfully:{removed}")
            return
        else:
            print("No ID found")

def main():
    books = load_book()
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter choice:").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            update_book(books)
        elif choice == "5":
            delet_book(books)
        elif choice == "6":
            break
        else:
            print("Invalid choice")
    print("Goodbye")

if __name__ == "__main__":
    main()
        
        