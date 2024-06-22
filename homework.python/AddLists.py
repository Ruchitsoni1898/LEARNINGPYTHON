lst1 = [1,2,3,4,5]
lst2 = [5,6,7,8,9]

new_lst =[]
for i in range(0,len(lst1)):
    new_lst.append(lst1[i]+lst2[i])
print(new_lst)