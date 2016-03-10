import time
"""
Author: Harshil Jethava
Title: Bubble sorting algo in python 3.x

Statement :Given a disordered list of integers (or any other items),
rearrange the integers in natural order.

Demo Input: [99,85,86,41]
Demo Output: [41,85,86,41]

Time Complexity of Solution:
Best O(n^2); Average O(n^2); Worst O(n^2).

Program demostrate bubble sorting algorithm in python
First of all,user has to provide limit count for how many number should be \
sorted .
After entered limit,user has to enter same number of elements only in interger form.
Not float or other datatype should be accepted.
"""
print("\n\t\t<< Bubble sorting algorithm in python 3>>")
n=0
n=int(input("\nHow many elements you want to add in bubble array ?"))
print("\nPlease enter",n,"<integer> elements for bubble sorting algo")
bubble=[]
j=0
#print(type(bubble))
for i in range(n):
    print("\nEnter element for position no:",i)
    j=int(input())
    bubble.append(j)
    i+=1
print("\nStoring position of elemets is:")
for i in range(len(bubble)):
    print(bubble[i],"is stored at position",i)

print("Your developed array for bubble sort is : ",bubble)
k=0
t1=time.clock()
for k in range(len(bubble)):
    for i in range(len(bubble)-1):
        if bubble[i+1]<bubble[i]:
            swap=bubble[i]
            bubble[i]=bubble[i+1]
            bubble[i+1]=swap
        else:
            i+=1
    k+=1
t2=time.clock()
print("\n\nAFTER WORK  ")

print(bubble)
print("\nTime taken to sort elements : ",t2-t1," second(s)")
