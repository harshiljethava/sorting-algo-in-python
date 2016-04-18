import time
print("\n\tFactorial using recursive method\n")
print("Enter number for finding Factorial\n ")
n=int(input())

def facrec(n):
    fans=1
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            fans=i*facrec(i-1)
    return fans
t1=time.clock()
print("Factorial of ",n,"is :",facrec(n))
t2=time.clock()
print("\nExecution time :",t2-t1)
