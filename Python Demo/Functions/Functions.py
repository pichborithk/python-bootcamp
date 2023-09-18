# Default Arguments
def a(b="b"):
    print(b)


a()
a("c")


def c(name, location):
    print(name)
    print(location)


# Positional Arguments
c("David", "Paris")
# Keyword Arguments
c(location="London", name="John")


def d(e):
    """
    docstring to add detail to functions
    """
    return e + 1


# Unlimited Arguments
def f(*g):
    # g is unlimited arguments in form of tuples
    for n in g:
        print(n)


f(1, 3, 5)


def h(**i):
    # i is unlimited keyword arguments in form of dictionary
    print(i)
    for key, value in i.items():
        print(key, value)


h(a=1, b=2, c=3)


def j(k: str, m: int) -> int:
    print(k)
    return m
