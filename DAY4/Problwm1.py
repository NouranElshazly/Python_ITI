# 1. We need to implement a python class that
# represents the queue data structure. The class
# should have these operations:
# a. insert(value) => which inserts a new value at
# the rear of the queue
# b. pop() => which returns and removes a value
# from the front of the queue. We should return
# None and print a warning message if we tried
# to pop value from an empty queue
# c. is_empty() => which returns True or False to
# represent whether the queue is empty or not.
class Queue:
    store=[]
    def __init__(self,name):
        self.name = name 
        self.list1=[]
        Queue.store.append(self)
# a - insert method
    def insert(self,item):
        self.list1.append(item)
        return self.list1
# b- check if the list is empty or not
    def is_empty(self):
        if len(self.list1)==0:
            return True

# c - pop method 
    def pop(self):
        if self.is_empty():
            print("You pop from an empty list !!")
        return self.list1.pop(0) #FIFO (QUEUE)
    
    @classmethod 
    def save(cls,filename):
        with open(filename,'w') as f:
            for i in cls.store:
                f.write(f"{i.name}*{i.list1}\n")
    @classmethod 
    def load(cls, name, filename):
        try:
            with open(filename, 'r') as f1:
                lines = f1.readlines()  
                for line in lines:
                    if line:
                        name_in_file, items_str = line.split("*")
                        if name_in_file == name:  
                            items_list = eval(items_str)  
                            queue = Queue(name)  
                            queue.list1 = items_list  
                            return queue         
        except Exception :
            print("this file name is not exist")

    def __str__(self):
        return f"Queue Name = {self.name} : items = {self.list1}" 
    
# test
q1 = Queue("first queue")
q1.insert(1)
q1.insert(2)
q1.save("file4.txt") 

q2 = Queue("second queue")
q2.insert(3)
q2.insert(4)
q2.save("file4.txt")  
x = Queue.load('first queue',"file4.txt")
print (x) #print address --> __Str__

y= Queue.load("second queue" ,"file4.txt")
print(y)

class newQueue(Queue):
    def __init__(self,name,size):
        super().__init__(name)
         #from the parent class 
        self.size=size

    def insert(self, value):
        if len(self.list1)>=self.size: #out of range
            raise IndexError("Queue reatched the max size !!")
        super().insert(value) # add in list1


# test this part 
q2=newQueue("thid queue",4)
try:
    q2.insert(1)
    q2.insert(3)
    q2.insert(8)
    q2.insert(30)
    # q2.insert(90) #raise index error as the size is 4
    print(q2.list1)
    print("Done")
except IndexError as e :
    print(e)
