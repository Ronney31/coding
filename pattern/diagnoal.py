#left Diagnoal
10000
01000
00100
00010
00001
print "#"*15
for i in range(5):
    for j in range(5):
        if(i==j):
            print "1",
        else:
            print "0",
    print "\n"



#right Diagnoal
00001
00010
00100
01000
10000
print "#"*15
p=4
for i in range(5):
    for j in range(5):
        if(p==j):
            print "*",
        else:
            print "0",
    print "\n"
    p-=1
