# 2. Create a list of strings , Add to it yourname then
# Write the list to a new File .

#creat list
list1 = ["hello" , "python"]
# add to it my name
list1.append("nouran")
#write list to new file 
with open("new.txt","w") as f2:
     for l in list1:
          f2.write(l + '\n')
print("Done !")
