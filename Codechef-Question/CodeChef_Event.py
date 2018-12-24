#https://www.codechef.com/problems/EVENT
t=int(input())
day = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" , "friday"]
for _ in range(t):
    s,e,l,r = map(str,input().strip().split())
    l=int(l)
    r=int(r)
    lst =[]
    mod = (day.index(e)-day.index(s)+1)%7
    
    for i in range( l, r+1 ):
        if ( i % 7 == mod ):
            lst.append(i)
    
    if(len(lst) == 0):
        print ("impossible")
    elif( len(lst) == 1):
        print (lst[0])
    else:
        print ("many")
 
