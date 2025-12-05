class A:
    def method(self):
        print("from A")

class B(A):
    def hello(self):
        print("from B")

class C(A):
    def hello(self):
        print("from C")


class D(B, C):
    def hello(self):
        print("from D")

d = D()

print(D.mro())
d.method()