class cal4:
    def sdata1(self,n1):
        self.n1 = n1
        return self.n1
    def display(self):
        self.ans = self.n1 * self.n1
        print("Ans is:",self.ans)

squa = cal4()
squa.sdata1(5)
squa.display()