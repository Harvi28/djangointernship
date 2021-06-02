class cal3:
    def __init__(self,p,r,n):
        self.p = p
        self.r = r
        self.n = n

    def calInterest(self):
        self.ans1 = (self.p * self.r * self.n) / 100
        return self.ans1

    def display1(self):
        print("Interest is:",self.ans1)

Interest = cal3(900,2,2)
Interest.calInterest()
Interest.display1()