# Write a Program that takes a list of 5 numbers
# [3,6,4,0,8] then
# a. Remove the last element in list .
# b. Add in the second place ‘R’.
# c. Ask the user to input specific number in list
# then delete it { by taking the list element not
# index}.
list1=[]
for i in range(5):
    number= int(input(f"Please Enter list elements {i+1}:"))
    list1.append(number)
print(list1)
# a. Remove the last element in list .
list1.pop()
print(list1)
# b. Add in the second place ‘R’.
list1.insert(1,'R')
print(list1)
# c. Ask the user to input specific number in list
element=int(input("Enter Your element you want to change :"))
value = input("Enter the value for your element :")
list1.insert(element,value)
print(list1)
# then delete it { by taking the list element not
# index}.
list1.remove(list1[0])
print(list1)