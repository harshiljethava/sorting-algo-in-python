#import decimal
import random
print("\n\t<< LINEAR SEARCH ALGORITHM >>\n\n")
print("You can store elements with following options :\
	\n1)random static //machine generated random array \n2)custom // create by your own brain")
op=int(input())
n=0
fno=0
search_array=[]
i=0
def linear_search(n,fno):

	while(i<n):
		j=search_array[i]
		print("j:",j)
		print("i",i)
		print("n",n)
		print("fno",fno)
		if j is fno:
			print("matched")
			print("Your number is located on :",i+1)
			break
		else:
			print("not matched")
			return "Your number is not in list"

if op==1:
	print("random elements are:")
	print("How many elements you want to store ?")
	ranlim=int(input())
	print("\n\nYOUR ",ranlim,"  RANDOM NUMBER WILL GENERATE IN RANGE OF <1 TO 100000>\n")
	i=0
	for i in range(ranlim):
		search_array.insert(i,random.randrange(100000))

	print("Your array of ",ranlim," is :\n",search_array)
	print("Enter number you are looking for")
	fno=int(input())
	#ranno=random.randrange(0,ranno)
	#print("rano",ranno)
	print(linear_search(ranlim,fno))
elif op==2:
	
	
	#search_array=[]
	print("custom elements are :")
	print("How many elements you want to store in array")
	n=int(input())
	
	print("please provide ",n," elements to store")
	i=0
	for i in range(n):
		j=0
		j=int(input())
		search_array.insert(i,j)

	print("array: ",search_array)

	print("Enter number you want to search")
	
	fno=int(input())

	print(linear_search(n,fno))
else:
	print("Invalid input !! please provide proper input")

#print(search_array)

