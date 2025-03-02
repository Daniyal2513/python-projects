import random

def number_guessing_game():
    secret_num = random.randint(1,100)
    attemp = 0

    print("Welcome to number guessing game")
    print("I have choosen number between 1 to 100 and you have to choose the correct number")

    while True:
        try:
            guess = int(input("Enter guess:"))
            attemp +=1

            if guess < secret_num:
                print("Guess is too low")
            elif guess > secret_num:
                print("Guess is to high")
            else:
                print(f"Congratulation you guess the correct number in {attemp} attemp")
                break
            
        except ValueError:
            print("Invlid input, Please enter number")

if __name__ == "__main__":
    number_guessing_game()