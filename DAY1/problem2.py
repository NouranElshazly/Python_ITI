#Write a function that accepts two arguments (length,start) to generate an array of a specific length filled with integer numbers increased by one from start.
length = int(input("Enter the length of array : "))
start = int(input("Enter the Start of array : "))

def fn(length , start):
    arr=[]
    for i in range(length):
        arr.append(start+i)
    return arr
# print(fn(13,4))
print(fn(length,start))