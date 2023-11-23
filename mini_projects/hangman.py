import random

# List of words for the game
words = ["python", "hangman", "programming", "computer", "developer"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

# Main game loop
def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if set(word_to_guess).issubset(set(guessed_letters)):
                print("You won! The word was: " + word_to_guess)
                break
        else:
            attempts -= 1
            print("Wrong guess. You have", attempts, "attempts left.")

    if attempts == 0:
        print("You ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
