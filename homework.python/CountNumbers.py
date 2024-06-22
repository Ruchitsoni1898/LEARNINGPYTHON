list =["2","6","7","4","5"]
num="+491793963161"
count=0
for character in num:
    if character in list:
        count+=1
        print(count)