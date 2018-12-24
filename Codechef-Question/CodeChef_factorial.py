#https://www.codechef.com/problems/FLOW018
'''
for _ in range(int(input())):
    no = int(input())
    fab = 1
    for i in range (2,no+1):
        fab*=i
    print (fab)
'''
#rec

for _ in range(int(input())):
    no = int(input())
    def fab (n):
        if n == 0 or n==1 :
            return 1
        return(n * fab(n-1))
    print (fab(no))
