import random
import time

def print_rules():
    print("\n--- GAME RULES ---")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'score' to view current scores.")
    print("Type 'rules' to view the rules again.")
    print("Type 'reset' to reset the scores.")
    print("Type 'quit' to exit the game.\n")

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors', 'score', 'rules', 'reset', 'quit']:
            return choice
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win this round!")
    else:
        print("Result: Computer wins this round!")

def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("=== Welcome to Rock-Paper-Scissors Game! ===")
    print_rules()

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()

        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score} | Computer: {computer_score}")
            break
        elif user_choice == "rules":
            print_rules()
            continue
        elif user_choice == "score":
            print(f"Current Score - You: {user_score} | Computer: {computer_score}")
            continue
        elif user_choice == "reset":
            user_score = 0
            computer_score = 0
            round_number = 1
            print("Scores have been reset.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play another round
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ['yes', 'y']:
                round_number += 1
                break
            elif play_again in ['no', 'n']:
                print("\nThanks for playing!")
                print(f"Final Score - You: {user_score} | Computer: {computer_score}")
                return
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()