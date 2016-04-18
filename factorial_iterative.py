import time
print("\n\tFactorial using iterative method\n")
print("Enter number for finding Factorial\n ")
n=int(input())

def fac(n):
    fans=1
    if n==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fans=fans*i
    print("Factorial of ",n,"is :",fans)
t1=time.clock()
fac(n)
t2=time.clock()
print("\nExecution time :",t2-t1)
