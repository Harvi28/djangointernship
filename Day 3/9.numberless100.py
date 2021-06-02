n = int(input("Enter number:"))
if(n<100):
    print("number is less than 100")
    if(n%2==0):
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is bigger than 100")