import random
selection=[]

def best(n):
    print("passed n :",n)
    for i in range(n):
        selection.insert(i,i)
    return selection
def worst(n):
    selection.clear()
    print("passed n :",n)
    j=0
    for i in range(n,0,-1):
        selection.insert(j,i)
        j+=1
    return selection

def avg(n):
    selection.clear()
    print("enter your limit ")
    n1=int(input("starting point"))
    n2=int(input("ending point"))
    for i in range(n):
        selection.insert(i,random.randrange(n1,n2))
    return selection
