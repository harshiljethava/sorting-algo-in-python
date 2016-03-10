import time
print("\n\t<<Insertion sort algo in python 3.x>>")
n=0
print("How many number you want to add in array ?")
n=int(input())
print("Please enter",n,"integer elements for storing in array")
ins=[]
j=0
for i in range(n):
    print("Enter element to store at position",i)
    j=int(input())
    ins.append(j)
index,k=0,1
for i in range(n):
    currval=ins[i]


print("\nYour constructed array for insertion sort")
print(ins)
