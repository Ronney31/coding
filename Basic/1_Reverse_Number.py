# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:42:03 2018

@author: Sardar
"""

N = int(input("Enter a number:- "))
lst = list(int(a) for a in str(N))
#lst1 = list(int())
lst.reverse()
#print (lst)
flg=0
for i in lst:
    if(i!=0):
        flg=1
    if(flg==1):
        print (i,end="")

 
