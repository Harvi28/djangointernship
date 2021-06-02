class cal2:
    def setdata(self):
        self.radius = float(input("Enter radius:"))

    def area(self):
       self.area = 3.14 * self.radius * self.radius
       return self.area

    def display(self):
        print("Ans is:",self.area)

circle = cal2()
circle.setdata()
circle.area()
circle.display()