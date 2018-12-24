#https://www.codechef.com/problems/MXM
import math
t=int(input())
'''for _ in range(t):
    n,k = map(int,input().strip().split())
    p = list(map(int,input().strip().split()))
    a=[]
    for i in range(n):
        a.append(pow(k,p[i]))
    a.sort()
    for i in range(1,len(a)):
        if(sum(a[:-i]) < sum(a[-i:])):
            print (len(a[:-i]))
            break
'''
def bs(a,s,e):
    if not s<e:
        return e
    md = (s+e)//2
    if (sum(a[:md]) < sum(a[md:])):
        if (sum(a[:md+1]) < sum(a[md+1:])):
            return bs(a,md+1,e)
        else:
            return md
    else:
        return bs(a,s,md)
    
for _ in range(t):
    n,k = map(int,input().strip().split())
    p = list(map(int,input().strip().split()))
    a=[]
    for i in range(n):
        a.append(pow(k,p[i]))
    a.sort()
    print (bs(a,0,n-1))
