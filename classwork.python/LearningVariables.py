d = 20  #it is a global variable
def addition():
    a = 10  # it is a local variable
    print(a)
    print(d)
    global c # it is a global variable
    c = 30
def substration():
    #print(a)   # it will give the error because a is a local variable of addition function
    print(d)
    print(c)




addition()
substration()