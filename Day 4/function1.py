def myfunc():
    print("Hiiii")

def myfunc1(name):
    print("Hiiii",name)

def myfunc2():
    name = "Harvi"
    return name

def myfunc3(name):
    print("Hiiiii")
    return name
def myfunc4():
    name1="xyz"
    n1 = 10
    return name1,n1


myfunc() #you can call function for multiple types
myfunc()
myfunc1(20)
myfunc1("Harvi")
print(myfunc2())
name = myfunc3("Hv")
print(name)
name1,n1 = myfunc4() #we have to maintain the order
print("Name is:",name1)
print("Number is:",n1)