# Write a Python program to convert two lists into a
# dictionary in a way that item from list1 is the key
# and item from list2 is the value.
list1 = [1,2,3,4,5]
list2=["nouran","mohammed","sama","basma","mariam"]
dic={}
for i in range (len(list1)):
    values={list1[i]:list2[i]}
    dic.update(values)
print(dic)