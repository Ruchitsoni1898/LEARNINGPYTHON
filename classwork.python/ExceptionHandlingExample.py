#amount = 10000 # Syntax Error
#if(amount>2999)
    #print("you are eligible to purchase the Dsa Self paced")

#marks = 10000 # Zero division error
#a = marks/0
#print(a)

#x = hello #Name error
#y = 5
#z = x+y


a =int(input("Enter First No:"))
b= int(input("Enter Second No:"))
try:
 c = a/b
 print("Result:",c)
except:
    print("Cant divide to zero....!")
else:
    print("Ruchit....")
