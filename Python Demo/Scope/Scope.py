# Global Scope
a = "a"


def b():
    # Local Scope
    c = "c"
    print(c)


if a == "a":
    # Global Scope
    d = "d"
else:
    # Global Scope
    d = "e"

print(d)

for n in range(1, 4):
    # Global Scope
    f = n
    print(f)

print(f)


# Modify Global Variable
g = 1


def h():
    global g
    g += 1
    print(g)


h()
print(g)
