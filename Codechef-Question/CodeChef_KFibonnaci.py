#https://www.codechef.com/problems/KFIB
n,k=map(int,input().strip().split())
a=[]
for i in range(1,n+1):
    if(i<=k):
        a.append(1%1000000007)
    elif(i>k):
        a.append((sum(a[-k:]))%1000000007)
print (a[-1]%1000000007)
