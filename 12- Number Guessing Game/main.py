import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' of 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.\nGuess again.")
        return attempts - 1
    elif guess < answer:
        print("Too low.\nGuess again.")
        return attempts - 1
    else:
        print(f"You got it! The number was {answer}")
        return -1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    answer = random.randint(1, 100)
    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        attempts = check_answer(guess_number, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")


game()
