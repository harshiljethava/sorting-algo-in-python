"""
Created on Wed Mar 16 09:41:47 2016

@author: wajidarshad
Dynamic Programming Python implementation of Matrix
Chain Multiplication. See the Cormen book for details
of the following algorithm
"""
def MatrixChainOrder(p, n):
# For simplicity of the program, one extra row and one
# extra column are allocated in m[][]. 0th row and 0th
# column of m[][] are not used
m = [[0 for x in range(n)] for x in range(n)]
s = [[0 for x in range(n)] for x in range(n)]
# m[i,j] = Minimum number of scalar multiplications needed
# to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
# dimension of A[i] is p[i-1] x p[i]

# cost is zero when multiplying one matrix.
#for i in range(1, n):
#m[i][i] = 0

# L is chain length.
for L in range(2, n):
for i in range(1, n-L+1):
j = i+L-1
m[i][j] = float('inf')
for k in range(i, j):

# q = cost/scalar multiplications
q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
if q < m[i][j]:
m[i][j] = q
s[i][j] = k
return m,s
def optimal_parenthesis(s,i,j):
if i==j:
print "A%d"%i,
else:
print"(",
optimal_parenthesis(s,i,s[i][j])
optimal_parenthesis(s,s[i][j]+1,j)
print")",
p=[23,34,56,34,2299,33,44]
n=len(p)
m,s=MatrixChainOrder(p,n)
cost= m[1][n-1]
#s=matrix_chain_parenthesis(p)
print "Input: ",p
print "\nm: "
for i in range(1,n-1):
for j in range(1,n):
print "\t %d"%(m[i][j]),
print "\n"
print "\ns: "
for i in range(1,n-1):
for j in range(1,n):
print " %d"%(s[i][j]),
print ""

print "\nOptimal Parenthesis :"
optimal_parenthesis(s,1,n-1)
print"\n\n Total multiplication is : %d\n" %(cost)
