list =["a","e","i","o","u"]
word= "Ruchit"
count = 0
for character in word:
    if character in list:
        count+=1
    print(count)
