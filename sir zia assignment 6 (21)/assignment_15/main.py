#15. Method Resolution Order (MRO) and Diamond Inheritanceclass A:
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Example usage
d = D()
d.show()  # Output: B (MRO: D -> B -> C -> A)