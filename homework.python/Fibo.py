n = int(input("Enter a Number:"))
x=0
y=0
z=1

while(z<=n):
    print(z) # print z becasue we run it through while loop for fibonacci series.
    x=y
    y=z
    z = x+y
