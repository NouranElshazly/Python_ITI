#Write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"

number=int(input("Enter your number : "))
def check_number(num):
    if (num%3==0 and num%5==0):
        print("FizzBuzz")
    elif num%5==0:
        print("buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print("Your Number Is not divisible by 5 or 3")
       
check_number(number)