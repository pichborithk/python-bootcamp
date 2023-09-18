a = 1

b = 2

if a < 0:
    print("smaller")
elif a == 0:
    print("equal")
elif a <= 1:
    print("bigger")
else:
    print("else")

match b:
    case 0 | 1:
        print("smaller")
    case target if target in range(3, 10):
        print("bigger")
    case _:
        print("equal")

# Logical Operators
if a > 1 and b > 1:
    print("ok")
else:
    print("no")

if 0 < a < 2:
    print("ok")
else:
    print("no")

if a > 1 or b > 1:
    print("ok")
else:
    print("no")

if not a > 1:
    print("ok")
else:
    print("no")

my_list = [1, 2, 3, 4]

if a not in my_list:
    print("no")
elif b in my_list:
    print("ok")
else:
    print("else")


# Ternary Operator

c = 3 if a < b else 0

# Ternary Operator using Tuples
# In this example, we are using tuples to demonstrate ternary operator.
# We are using tuple for selecting an item and if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print.

d, e = 10, 20

print((e, d)[d < e])

# Ternary Operator using Dictionary

print({True: d, False: e}[d < e])

# Ternary Operator using Lambda

print((lambda: e, lambda: d)[d < e]())
