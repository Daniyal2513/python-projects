import json
import random
import os

file_name = "flashcard.json"

def load_flashcards():
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            try:
                return json.load(file)
            except (FileNotFoundError,json.JSONDecodeError):
                return []
    return []

def save_flashcards(flashcard):
    with open(file_name,"w")as file:
        json.dump(flashcard,file,indent=4)

def add_flashcard(flashcards):
    question  = input("Enter a question:")
    answer = input("Enter an answer:")
    flashcards = load_flashcards()
    flashcards.append({"question":question,"answer":answer})
    save_flashcards(flashcards)
    print("Flashcard added successfully!!")

def quiz_flashcard(flashcards):
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards to quiz")
        return
    
    random.shuffle(flashcards)
    for card in flashcards:
        user_answer = input(f"{card['question']}:")
        if user_answer.lower() == card['answer'].lower():
            print("Correct!")
        else:
            print("Wrong answer!!")

def main():
    flashcards = load_flashcards()
    while True:
        print("1. Add flashcard")
        print("2. Quiz flashcards")
        print("3. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            quiz_flashcard(flashcards)
        elif choice == "3":
            break
        else:
            print("Invalid choice!!")

if __name__ == "__main__":
    main()
