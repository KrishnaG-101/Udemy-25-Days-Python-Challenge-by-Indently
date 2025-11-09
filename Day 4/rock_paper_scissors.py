# This file contains simple rock paper scissors game which the user can play with the computer.

import random

options : dict[str, str] = {"r" : "Rock (🪨)",
                            "p" : "Paper (📄)",
                            "s" : "Scissors (✂️)"}

play_game_input = 'y'

while play_game_input.lower() != 'e':
    # Welcome display
    print("\n" + "=" * 40)
    print("Welcome to Rock, Paper and Scissors game, choose an option and play against the computer.")
    
    # Choice selection and display
    user_choice_input : str = input("\nEnter R for Rock (🪨), P for Paper (📄) or S for Scissors (✂️): ").strip()
    computer_choice : str = random.choice(tuple(options))
    print("\n" + "-" * 30)
    print(f"You:            {options.get(user_choice_input.lower())}")
    print(f"Computer:       {options.get(computer_choice)}")
    
    
    # Processing and Result display
    if user_choice_input.lower() == computer_choice:
        print(f"\nYou chose {options.get(user_choice_input.lower())} and computer chose {options.get(computer_choice)}, It's a Tie.")
    elif user_choice_input.lower() == "r" and computer_choice == "s":
        print(f"\nYou chose {options.get(user_choice_input.lower())} and computer chose {options.get(computer_choice)}, You Won.")
    elif user_choice_input.lower() == "s" and computer_choice == "p":
        print(f"\nYou chose {options.get(user_choice_input.lower())} and computer chose {options.get(computer_choice)}, You Won.")
    elif user_choice_input.lower() == "p" and computer_choice == "r":
        print(f"\nYou chose {options.get(user_choice_input.lower())} and computer chose {options.get(computer_choice)}, You Won.")
    else:
        print(f"\nYou chose {options.get(user_choice_input.lower())} and computer chose {options.get(computer_choice)}, You Lost.")

    print("-" * 30)
    
    # Taking input to play again
    play_game_input : str = input("\nPress E to exit or Any other key to play again: ")

print("\nThank you for playing the game, I hope you enjoyed.")
print("=" * 40)