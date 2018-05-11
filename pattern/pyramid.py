'''
     *
    ***
   *****
  *******
 *********
***********
'''



def gn(n):
    sp=n-1
    s=1
    for i in range(n):
        for j in range(sp):
            print " ",
        sp-=1
        for j in range(s):
            print "*",
        print "\n"
        s=s+2

r=int(input("Enter the height of the pyramid:- "))
gn(r)
