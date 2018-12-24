#https://www.codechef.com/DEC18B/problems/CHFINTRO
n,r = map(int,input().strip().split())
a=[]
for _ in range(n):
    a.append(int(input()))
for i in a:
    if i<r:
        print ("Bad boi")
    else:
        print ("Good boi")
