class arith:
    def __init__(self):
        self.n1 = int(input("Enter 1 st number:"))
        self.n2 = int(input("Enter 2 nd number:"))

    def add(self):
        self.ansa = self.n1 + self.n2
        return self.ansa
    def subs(self):
        self.anss = self.n1 - self.n2
        return self.anss
    def mult(self):
        self.ansm = self.n1 * self.n2
        return self.ansm
    def display(self):
        print("Addition is:",self.ansa)
        print("Substraction is:", self.anss)
        print("Multiplication is:", self.ansm)
a = arith()
a.add()
a.subs()
a.mult()
a.display()

