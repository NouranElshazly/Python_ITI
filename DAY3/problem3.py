#problem4 in lab 3
from calculator.my_functions import *
while True:
    try :

            operand =int(input('''
            Hello from my simple calculator please enter your number for operation :
                                        0-> sum
                                        1-> substract 
                                        2-> divide
                                        3->multiply   : '''))

            num1= int (input("Enter first number : "))
            num2 =int(input("Enter second number : "))
            if operand == 0:
                   result =add_fn(num1,num2)
                   print("result = " ,result)
            elif operand ==1:
                   result=substract(num1,num2)
                   print("result",result)
            elif operand==2:
                   result=divide(num1,num2)
                   print("result = ",result)
            elif operand==3:
                   result=multiply(num1,num2)
                   print("result = ",result)
            break
    except ValueError as v :
           print(v)
    except ZeroDivisionError as z :
           print(z)       
    except Exception as  e:
            print("Please Enter a validNumber !")

