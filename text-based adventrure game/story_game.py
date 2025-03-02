def start_game():
    print("Welcome To Adventure Game.")
    print("Story: The Lost Island Adventure.")
    print("Waking up on the shore of island. You have two choices: ")
    print("1. Enter the dense jungle to search for help or treasure.")
    print("2. Follow the beach to find remains of their ship or another way off the island.")

    choice1 = input("Enter 1 or 2:")

    if choice1 == "1":
        print("\n You follow the Jungle path.")
        print("You hear rustling leaves and see two paths.")
        print("1. A dark cave with strange carvings.")
        print("2. A river with a broken bridge.")

        choice2 = input("Enter 1 or 2:")

        if choice2 == "1":
            print("\n If you Enter the cave.")
            print("You find an ancient scroll that hints at the Golden idols location.")
            print("But suddenly,a giant spider block the exit")
            print("Game Over!!!")

        else:
            print("\n You go to that broken bridge.")
            print("The Bridge is weak and the bridge collapses.")
            print("If you swim,a mysterious whirlpool pulls them into an underground temple")

            print("You win!!!!!!")
    elif choice1 == "2":
        print("\n You go on beach Path")
        print("You find a small hut and footprints in the sand.")
        print("1. Entering the hut cautiously.")
        print("2. Following the footprints into the jungle.")

        choice2 = input("Enter 1 or 2:")
        if choice2 == "1":
            print("\n If you entering the Hut curiously")
            print("There's a map, but suddenly, the hut’s owner returns!")
            print("Game Over")
        else:
            print("\n If they follow footprints")
            print("They find a broken compass and a clue about the island’s secrets.")
            print("You win!!!!")

    else:
        print("Invalid choice. Please restart the game.")

start_game()