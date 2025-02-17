#Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.
value = str(input("Enter Your string :"))
counter = 0 
for i in value:
    if (i == 'a' or i=='e' or i=='o' or i=='u' or i=='i'):
        counter +=1
print(counter)    