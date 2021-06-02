class cal1:
    def setdata(self,a,b,c):
        self.sum1= a+b+c
        return self.sum1

    def display(self):
        print("Ans is:",self.sum1)

calculate= cal1()
calculate.setdata(10,20,30)

calculate.display()