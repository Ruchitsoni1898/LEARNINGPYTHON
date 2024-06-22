levels = 5 # define number of levels for pyramid

i = 1 #initialize level variable

while i <=levels: #loop through each level of pyramid
    #Print Spaces
    b=1
    while b<=levels - i:
        print("",end="")
        b = b+1

    #Print Stars
    j=1
    k=2*i-1
    while j<=k:
        print("*" ,end="")
        j = j+1
    print()
    i = i+1
