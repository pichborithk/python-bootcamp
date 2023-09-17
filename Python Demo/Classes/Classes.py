class A:
    def __init__(self, b, c):
        print("New object has been create by class")
        self.b = b
        self.c = c
        self.d = "d"

    def e(self):
        print("e")


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
print(d.b, d.c, d.e)
