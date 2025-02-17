#problem3 in lab3
#addition function
def add_fn (num1,num2):
    return num1+num2

#substract function
def substract(num1,num2):
    if num1 == 0 or num2==0 :
        raise ValueError("Substracting from zero number !! ")
    return num1-num2

#multiply function
def multiply (num1,num2):
    if num1 == 0 or num2==0 :
        raise ValueError("Substracting from zero number !! ")
    return num1*num2

#divide function
def divide(num1,num2):
    if num1 == 0 or num2==0 :
        raise ZeroDivisionError("Can not divide by zero number !! ") 
    return num1/num2
