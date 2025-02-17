
# 1. Write a Python program to read a file line by line
# and store it into a list.

with  open("file1.txt",'r') as f1:
        outputline=f1.readlines()
        print(outputline)
    