# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:39:33 2018

@author: Sardar
"""

def maxNumber(a):
    sorted(a)
    a.reverse()
    flg = None
    for i in a:
        num = str(i)
        if not flg:
            flg = num
        else:
            n1 = flg + num
            n2 = num + flg
            if n1 >= n2:
                flg = n1
            else:
                flg = n2
    return flg

n=int(input())
a=list(map(int,input().strip().split()))
#a=[54, 546, 548, 60]
print (maxNumber(a))
