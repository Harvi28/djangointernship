def calSum(n1,n2):
    return n1+n2

ans = calSum(10,30)
print("Ans is:",ans) #function with normal argument

def calSum1(n1=24,n2=16):
    return n1+n2

ans1 = calSum1() #if we will not give argument then it will take default argument
print("Ans is:",ans1)
ans2 = calSum1(13,39)
print("Ans is:",ans2)

def calSum2(n1,n2):
    print("Ans is",n1+n2)

calSum2(n2 = 6,n1 = 16)
