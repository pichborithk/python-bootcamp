import random

from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []
for _ in range(word_length):
    display += "_"

guessed_list = []


print(logo)
print(display)
# print(f"Pssst, the solution is {chosen_word}.")


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_list:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = guess

    guessed_list += guess
    print(f"{stages[lives]}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win.")
