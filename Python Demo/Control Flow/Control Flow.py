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


# Logical Operators
if a > 1 and b > 1:
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