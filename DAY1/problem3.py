arr=[]
for i in range(5):
    number=int(input(f"Enter arr elements {i+1} :"))
    arr.append(number)
    
print(arr) 
sort_arr=sorted(arr)
print(sort_arr)
reversedArr = sorted(arr,reverse=True)
print(reversedArr)


