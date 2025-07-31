import random

# Predefined list of words
words = ["apple", "tiger", "robot", "chair", "water"]
secret_word = random.choice(words)  # Randomly select a word
guessed_letters = []                # List to store correct guesses
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("_ " * len(secret_word))  # Display blanks for the word

while wrong_guesses < max_wrong:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        wrong_guesses += 1

    # Show current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if user has guessed all letters
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break
else:
    print(f"\n💀 Game Over! The word was '{secret_word}'.")
