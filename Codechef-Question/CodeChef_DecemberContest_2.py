#https://www.codechef.com/DEC18B/problems/CHFIDEAL
import random
a=[1,2,3]
ran = random.choice(a)
print (ran)
a.remove(ran)
t=int(input())
a.remove(t)
print (a[0])
