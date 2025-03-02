import json
import os

file_name = "quiz.json"

def load_question():
    if os.path.exists(file_name):
        with open(file_name, "r")as file:
            return json.load(file)
    
    return []

def save_question(questions):
    with open(file_name, "w") as file:
        json.dump(questions,file,indent= 4)

def play_quiz():
    questions = load_question()

    if not questions:
        print("No question available, add questions first!")
        return
    score = 0
    print("Welcome to Quiz game,Lets begin.")
    
    for i ,q in enumerate(questions,1):
        print(f"{i}.{q['questions']}")
        for j,option in enumerate(q['options'],1):
            print(f"{i}.{option}")
    
        try:
            user_answer = int(input("Enter your answer(1-4):"))-1
            if 0<=user_answer<len(q['options']):
                if q['options'][user_answer]==q['answer']:
                    print("✅ Correct!\n")
                    score+=1
                else:
                 print(f"❌ Wrong! Correct answer: {q['answer']}\n ")
            else:
             print("Invalid choice,Skipping!")
        except ValueError:
            print("Invalid Input.")

    print(f"Game over, Your score: {score}/{len(questions)}")

def add_question():
    questions = input("Enter question:")
    options = []

    for i in range(4):
        option = input(f"Enter option{i+1}:")
        options.append(option)

    correct_answer = input("Enter the correct option(must match one of the option exactly)")

    if correct_answer  not in options:
        print("⚠ Error: The correct answer must be one of the provided options.")
        return

    new_question = {"questions":questions , "options": options, "answer":correct_answer} 

    questions = load_question()
    questions.append(new_question)
    save_question(questions)

def view_question():
    questions = load_question()
    if not questions:
        print("No question found.")
        return
    for i,q in enumerate(questions,1):
        print(f"{i}.{q['questions']}:(Answer:{q['answer']})")

def delete_question():
    questions = load_question()

    if not questions:
        print("No question to delete")
    
    for i,q in enumerate(questions,1):
        delete_question = questions.pop(i)
        save_question(questions)
        print("Question deleted successfully.")

def main():
    while True:
        print("1. Play Quiz")
        print("2. Add Question")
        print("3. View Questions")
        print("4. Exit")

        choice = input("Enter your choice:")
        
        if choice == "1":
            play_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            view_question()
        elif choice == "4":
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()

    
    
    