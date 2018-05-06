#printing Diamond
##0000-0000
##000-0-000
##00-000-00
##0-00000-0
##-0000000-
##0-00000-0
##00-000-00
##000-0-000
##0000-0000
print ("#"*15)
#i=j=9
p=q=5
r=-3
s=13
for i in range(1,10):
    for j in range(1,10):
        if(j==p and j==q):
            #print j,
            print('X'),
        elif(j==p and j!=q):
            #print j,
            print('X'),
        elif(j==q and j!=p):
            #print j,
            print('X'),
        elif(p<1 and j==r and j==s):
            #print j,
            print('X'),
        elif(p<1 and j==r and j!=s):
            #print j,
            print('X'),
        elif(p<1 and j==s and j!=r):
            #print j,
            print('X'),
        else:
            print ("0"),
    print ("\n")
    q+=1
    p-=1
    r+=1
    s-=1
