# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:00:56 2018

@author: Sardar
"""
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if(n%i==0):
            return False
    return True
def nearestPrime(n):
    if(n==0 or n==1 or n==2):
        return (abs(n-2))
    if(isPrime(n)):
        return (0)
    else:
        prime1=0
        prime2=0
        i=1
        while(True):
            if(isPrime(n-i) == 1):
                prime1=n-i
                return abs(n-prime1)
            if(isPrime(n+i) == 1):
                prime1=n+i
                return abs(n-prime1)
            i+=1

num=int(input("Please provide Current Position:- "))
print (nearestPrime(num))
#print(nearestPrime(2000000000))
#print(nearestPrime(1800000001))

