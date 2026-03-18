# adventure_game.py
# A simple text-based adventure game where the player searches for a legendary treasure


def start_game():
    """Begin the adventure by greeting the player and asking for their first choice."""
    print("Welcome to the Adventure Game!")
    name = input("What is your name, explorer? ")
    print(f"Hello, {name}! Your quest is to find the legendary treasure.")
    print("You stand at a crossroads. Do you want to explore the (1) dark forest or (2) mysterious cave?")
    choice = input("Enter 1 for forest or 2 for cave: ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    else:
        print("That is not a valid option. Let's try again.")
        start_game()


def forest_path():
    """Handle the scenario when the player chooses the forest."""
    print("You step into the dark forest. The trees loom overhead and you hear a river nearby.")
    print("Do you (1) follow the sound of the river or (2) climb a tall tree to get a better view?")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("You follow the river and slip on a rock, injuring yourself. The quest ends here.")
        play_again()
    elif choice == "2":
        print("From the top of the tree you spot a glint of gold — the treasure is nearby!")
        print("Congratulations, you have found the treasure and won the game!")
        play_again()
    else:
        print("That choice doesn't make sense. The forest swallows you.")
        play_again()


def cave_path():
    """Handle the scenario when the player chooses the cave."""
    print("You enter the mysterious cave. It's dark and you can barely see.")
    print("Do you (1) light a torch or (2) proceed in the dark relying on your other senses?")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("The torch reveals ancient markings that lead you to the treasure chamber!")
        print("Congratulations, you have found the treasure and won the game!")
        play_again()
    elif choice == "2":
        print("You stumble in the darkness and fall into a pit. The quest ends here.")
        play_again()
    else:
        print("Your hesitation causes the cave to collapse. You barely escape.")
        play_again()


def play_again():
    """Ask the player if they want to restart the adventure."""
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower().startswith('y'):
        start_game()
    else:
        print("Thanks for playing! Farewell, explorer.")
        exit()


# Call start_game if this script is run directly
if __name__ == "__main__":
    start_game()
