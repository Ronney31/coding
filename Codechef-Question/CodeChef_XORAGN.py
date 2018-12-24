#https://www.codechef.com/problems/XORAGN
t=int(input())
'''for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    b=[]
    for i in range(n):
        for j in range(n):
            b.append(a[i]+a[j])
            
    res=b[0]
    for i in range(1,len(b)):
        res=res^b[i]
    print (res)
'''
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    res=0
    for i in range(n):
        if(i==0):
            res=a[i]
        else:
            res=res^a[i]
            
    print (res*2)
