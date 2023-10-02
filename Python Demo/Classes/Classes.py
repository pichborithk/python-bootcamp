class A:
    def __init__(self, b, c):
        print("New object has been create by class")
        self.b = b
        self.c = c
        self.d = "d"

    def e(self):
        print("e")

    # __str__ is for print
    def __str__(self):
        return {"b": self.b, "c": self.c, "d": self.d}


a = A(c="c", b="b")
print(a.b)


# Inheritance
class D(A):
    def __init__(self, b, c, f):
        super().__init__(b, c)
        self.f = f

    def e(self):
        super().e()
        print("new e")

    def g(self):
        print("g")


d = D("b", "c", "f")
d.e()
print(d.b, d.c, d.f)


# Property and Decorator
class H:
    def __init__(self, j):
        self.j = j
        # Because we create getter (property) and setter (decorator) below
        # self.j will automatically call that method
        # so python will read self.j = j as self.j(j)

    # Getter
    @property  # property
    def j(self):
        return self._j
        # We need to use self._j as j property so that python not confuse it with j method

    # Setter
    @j.setter  # Decorator
    def j(self, k):
        self._j = k


h = H("j")
h.j = "k"
print(h.j)


# To make property immutable
class M:
    def __init__(self, n):
        self._n = n

    # Getter
    @property
    def n(self):
        return self._n
        # We need to use self._j as j property so that python not confuse it with j method

    # Setter
    @n.setter
    def n(self, p):
        if p == self.n:
            self._n = p


m = M("n")
print(m.n)
m.n = "p"
print(m.n)


# classmethod and staticmethod
class Q:
    q = "q"

    @classmethod
    def print(cls, r):
        print(cls.q, r)

    @staticmethod
    def s(t):
        print(Q.q)
        print(t)


Q.print("r")
Q.s("t")
q = Q()
print(Q.q)


# Operator overloading
class U:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        new_v = self.v + other.v
        # as long as "other" had the same attribute/property (v) as self
        # we can use any class as "other"
        return U(new_v)

    def __str__(self):
        return f"v = {self.v}"


u_1 = U(5)
u_2 = U(10)
new_u = u_1 + u_2
print(new_u)
