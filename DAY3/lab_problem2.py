# Write a function that accepts a number as a parameter. The function should return a number that’s the difference
# between the largest and smallest numbers that the digits can form in the number.
# ○
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123
# subtracted from 321.
def difference_of_largest_and_smallest(num):
    digits = []
    while num > 0:
        digits.append(num % 10)  
        num //= 10 
    digits.sort()  
    smallest_num = 0
    for i in digits:
        smallest_num = smallest_num * 10 + i    
    digits.sort(reverse=True)  
    largest_num = 0
    for i in digits:
        largest_num = largest_num * 10 + i   
    return largest_num - smallest_num

try:
    num =int(input("Please Enter a Number : "))
except Exception as e :
    print(e)
else:
    print(difference_of_largest_and_smallest(num))  
