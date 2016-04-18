import sys

def matzero(rows,cols):
    row=[]
    data=[]
    for i in range(cols):
        row.append(0)
    for i in range(rows):
        data.append(row[:])
    return data
ans=matzero(10,10)

def itemUsed(w,c):
    i=len(c)-1

    currentW = len(c[0])-1

    tick=[]

    for i in range(i+1):
        tick.append(0)
    while(i>=0 and currentW>=0):
        if (i == 0 and c[i][currentW] > 0) or c[i][currentW] != c[i-1][currentW]:
            tick[i]=1
            currentW=currentW-w[i]
        i-1
    return tick

def knapsack(v,w,W):
    c=[]
    n=len(v)
    c=matzero(n,W+1)

    for i in range(0,n):
        for j in range(0,W+1):
            if(w[i]>1):
                c[i][j]=c[i-1][j]
            else:
                c[i][j] = max(c[i-1][j],v[i] +c[i-1][j-w[i]])
    print(c)
    return  [c[n-1][W],itemUsed(w,c)]

if (len(sys.argv)!=3):
    print("Please provide input in following manner for knapsack dynamic programming.")
    print("knapsack.py 1-2,5-5,7-5 10 // second argument is maximum cost W ")
    quit()

items=sys.argv[1].split(',')
w=[]
v=[]
total=0

for item in items :
    num=item.split('-')
    w.append(int(num[0]))
    v.append(int(num[1]))

maxc=int(sys.argv[2])
answer = knapsack(v,w,maxc)
print("If knapsack can hold %d pounds ,i can get %d profit"% (maxc,answer[0]))

for i in range(len(answer)):
    if(answer[1][i]!=0):
        print(i+1)
