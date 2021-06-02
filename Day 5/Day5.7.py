class cal6:
    def setdata(self):
        self.length = float(input("Enter length:"))

    def area(self):
       self.area = self.length * self.length
       return self.area

    def display(self):
        print("Ans is:",self.area)

square = cal6()
square.setdata()
square.area()
square.display()