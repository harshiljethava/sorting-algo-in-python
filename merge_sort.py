import time,bwacase
n=0
print("enter your n")
n=int(input())
print("enter ",n,"elements")
#print(bwacase.best(n))
j=0
bmerge=[]
wmerge=[]
amerge=[]
'''
for i in range(n):
    j=int(input())
    merge.append(j)
#print(\n\nentered array: ,merge)'''
bmerge=bwacase.best(n)
print(bmerge)
print("\n\nBEST CASE entered array: ",bmerge)
t1=time.clock()
def mergeSort(bmerge):
    print("Splitting ",bmerge)
    if len(bmerge)>1:
        mid = len(bmerge)//2
        lefthalf = bmerge[:mid]
        righthalf = bmerge[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                bmerge[k]=lefthalf[i]
                i=i+1
            else:
                bmerge[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            bmerge[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            bmerge[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",bmerge)
t2=time.clock()
print("\n\narray After merge sort BEST: ",bmerge)

wmerge=bwacase.worst(n)
print("\n\tWORST array: ",wmerge)
t3=time.clock()
mergeSort(wmerge)
t4=time.clock()
print("\n\narray After merge sort WORST: ",wmerge)
print("\n\nexecution time for BEST CASE: ",t2-t1," seconds")
print("\n\nexecution time for WORST CASE: ",t4-t3," seconds")

amerge=bwacase.avg(n)
print("\n\tAVERAGE array: ",amerge)
t5=time.clock()
mergeSort(amerge)
t6=time.clock()
print("\nBEST CASE: Array after merge sort:",bmerge)
print("\nWORST CASE:Array after merge sort:",bmerge)
print("\nAVERAGE CASE:Array after merge sort:",bmerge)

print("\n\nexecution time for BEST CASE: ",t2-t1," seconds")
print("\n\nexecution time for WORST CASE: ",t4-t3," seconds")
print("\n\nexecution time for AVERAGE CASE: ",t6-t5," seconds")
