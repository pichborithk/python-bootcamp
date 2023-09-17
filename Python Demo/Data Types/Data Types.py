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

e = 5.5629234

print(round(e))
print(round(e, 4))
print(f"{e:.2f}")
f = 1000
print(f"{f:,}")
