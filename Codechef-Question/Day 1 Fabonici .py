#day 1 fabonici serise using  (Recursion, Memoization and Tabulation)

def recurs (n):
	if (n<=1):
		return n;
	res = (recurs(n-1) + recurs (n-2))
	return (res)

print (recurs (40))
a=input("enter to exit")
#print ("hello")