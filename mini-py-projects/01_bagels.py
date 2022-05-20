"""
Bagels
A deductive logic game where you must judge a number based on clues.
Link: https://inventwithpython.com/bigbookpython/project1.html#
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        f"""Bagels, a deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.
 
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
    """
    )

    while True:  # Main game loop
        # This stores the secret number that the player needs to guess
        secretNum = getSecretNum()
        print(f"I have thought up a number. You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print(f"You ran out of guesses. The answer was {secretNum}")

        # Ask player if they want to play again
        print("Do you want to play again? (yes/no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def getSecretNum():
    """
    Returns a string of NUM_DIGITS unique random digits
    """
    numbers = list("0123456789")  # Create a list of digits 0 to 9
    random.shuffle(numbers)  # Shuffle them into random order

    # Get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """
    Returns a string with pico, fermi, bagel clues for a guess
    and a secret number pair
    """
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give info away
        clues.sort()
        # Make a single string from the list of string clues
        return " ".join(clues)


if __name__ == "__main__":
    main()
