import time,bwacase
n=0
print("enter your n")
n=int(input())
print("enter ",n,"elements")
#print(bwacase.best(n))
j=0
bselection=[]
wselection=[]
aselection=[]
'''
for i in range(n):
    j=int(input())
    selection.append(j)
#print(\n\nentered array: ,selection)'''
bselection=bwacase.best(n)
print(bselection)
print("\n\nBEST CASE entered array: ",bselection)
t1=time.clock()
for k in range(len(bselection)-1,0,-1):
    max=0
    for i in range(1,k+1):
        if(bselection[i]>bselection[max]):
            max=i
    swap=bselection[k]
    bselection[k]=bselection[max]
    bselection[max]=swap
t2=time.clock()
print("\n\narray After selection sort BEST: ",bselection)


wselection=bwacase.worst(n)
print("\n\tWORST array: ",wselection)
t3=time.clock()
for k in range(len(wselection)-1,0,-1):
    max=0
    for i in range(1,k+1):
        if(wselection[i]>wselection[max]):
            max=i
    swap=wselection[k]
    wselection[k]=wselection[max]
    wselection[max]=swap
t4=time.clock()
print("\n\narray After selection sort WORST: ",wselection)
print("\n\nexecution time for BEST CASE: ",t2-t1," seconds")
print("\n\nexecution time for WORST CASE: ",t4-t3," seconds")

aselection=bwacase.avg(n)
print("\n\tAVERAGE array: ",aselection)
t5=time.clock()
for k in range(len(aselection)-1,0,-1):
    max=0
    for i in range(1,k+1):
        if(aselection[i]>aselection[max]):
            max=i
    swap=aselection[k]
    aselection[k]=aselection[max]
    aselection[max]=swap
t6=time.clock()
print("\nBEST CASE: Array after selection sort:",bselection)
print("\nWORST CASE:Array after selection sort:",bselection)

print("\n\narray After selection sort WORST: ",aselection)
print("\n\nexecution time for BEST CASE: ",t2-t1," seconds")
print("\n\nexecution time for WORST CASE: ",t4-t3," seconds")
print("\n\nexecution time for AVERAGE CASE: ",t6-t5," seconds")
