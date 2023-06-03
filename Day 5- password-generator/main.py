# Password Generator Project
import random
from characters import letters, numbers, symbols


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for n in range(0, nr_letters):
    # password += letters[random.randint(0,len(letters) - 1)]
    password += random.choice(letters)

for n in range(0, nr_symbols):
    # password += symbols[random.randint(0, len(symbols) - 1)]
    password += random.choice(symbols)

for n in range(0, nr_numbers):
    # password += numbers[random.randint(0, len(numbers) - 1)]

    password += random.choice(numbers)

print(password)

# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for n in range(0, nr_letters):
    # password_list.append(random.choice(letters))
    password_list += random.choice(letters)

for n in range(0, nr_symbols):
    # password_list.append(random.choice(symbols))
    password_list += random.choice(symbols)


for n in range(0, nr_numbers):
    # password_list.append(random.choice(numbers))
    password_list += random.choice(numbers)

random.shuffle(password_list)

print("".join(password_list))
