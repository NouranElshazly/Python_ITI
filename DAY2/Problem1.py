# Write a Python function to check whether a number
# falls in a given range. Range (-5, 5) -> return TRUE
number= int (input("Enter Your Number :"))
def number_check (num):
    if num in range(-5,6):
        print("True")
    else : 
        print("False")
number_check(number)