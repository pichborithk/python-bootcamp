# Ask user for their name:
# name = input("What is your name? ").strip().title()

# print(f"hello, {name}")
# print("hello,", name)

name = "David Beckham"
names = name.split(" ")
first, last = name.split(" ")

print(names)
print(first)

# String
a: str = "           a"

# Remove whitespace from string and capitalize
a = a.strip().title()

# Integer
b = 1
print(type(b))

c = 3
print(type(c))

# Float

d = c / b
print(type(d))

e = b // c
print("e:", e)
print("type e:", type(e))

f = 5.5629234

print(round(f))
print(round(f, 4))
print(f"{f:.2f}")
g = 1000
print(f"{g:,}")

# List

my_list = ["a", 1, True]

print(my_list[-1])
print(my_list[-2])

# Dictionary

my_dict = {"a": 0, 1: "b"}

print(my_dict["a"])
print(my_dict[1])

# Tuples
# tuples is immutable

my_tuples = (1, 2, 3)
