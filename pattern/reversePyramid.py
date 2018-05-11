'''
***********
 *********
  *******
   *****
    ***
     *
'''



def gn(n):
    sp=0
    s=n+(n-1)
    for i in range(n):
        for j in range(sp):
            print " ",
        sp+=1
        for j in range(s):
            print "*",
        print "\n"
        s=s-2

r=int(input("Enter the height of the pyramid:- "))
gn(r)
