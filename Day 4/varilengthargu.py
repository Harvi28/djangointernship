def sum(*a): #non keyword
    sum = 0
    for i in a:
        sum = sum+i
    print("Ans is:",sum)

sum(21,24)
sum(10,20,30)
def myfunction(**args):
    for i,j in args.items():
        print(i,j)
       # print(j)
myfunction(name="Harvi",id=1)
myfunction(name="HV",id=2)