class cal5:
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        self.ans = self.w * self.h
        return self.ans
    def display(self):
        print("Area of Rectangle:",self.ans)

rect = cal5(2,5)
rect.area()
rect.display()