from random import choice
from game_data import data
from art import logo, vs
import os


def print_account(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(pick, a_followers, b_followers):
    if pick == "a":
        return a_followers > b_followers
    else:
        return a_followers < b_followers
    # if a_followers > b_followers and pick == "a":
    #     return True
    # elif b_followers > a_followers and pick == "b":
    #     return True
    # else:
    #     return False

    # if a_followers > b_followers:
    #     return pick == "a"
    # else:
    #     return pick == "b"


account_a = choice(data)
account_b = choice(data)
while account_a == account_b:
    b = choice(data)
score = 0
game_over = False

while not game_over:
    print(f"Compare A: {print_account(account_a)}")
    print(vs)
    print(f"Against B: {print_account(account_b)}")

    pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(
        pick, account_a["follower_count"], account_b["follower_count"]
    )

    os.system("clear")
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        while account_a == account_b:
            account_b = choice(data)

    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
