num1 = int(input("Enter the first no:"))
num2 = int(input("Enter the second no:"))
num3 = int(input("Enter the Third No:"))

if num1 < num2 and num1 < num3:
    print("num1 is smaller")
elif num2 < num3 and num2 < num1:
    print("num2 is smaller")
elif num3 < num1 and num3<num2:
    print("num3 is smaller")
else:
    print("values are same")



