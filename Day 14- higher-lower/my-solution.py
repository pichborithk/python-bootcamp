from random import choice
from game_data import data
from art import logo, vs
import os

a = choice(data)
b = choice(data)
while a == b:
    b = choice(data)
score = 0
game_over = False

while not game_over:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    if a["follower_count"] > b["follower_count"]:
        answer = "a"
    else:
        answer = "b"

    pick = input("Who has more followers? Type 'A' or 'B': ")

    if pick.lower() == answer:
        score += 1
        a = b
        while a == b:
            b = choice(data)
        os.system("clear")
    else:
        game_over = True
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
