#printing LessThan sign
'''
0000X
000X0
00X00
0X000
X0000
0X000
00X00
000X0
0000X
'''
print "#"*15
p=4
l=-4
for i in range(9):
    for j in range(5):
        if(p==j and i<5):
            print ("X"),
        elif(i>=5 and j==l):
            print("@"),
        else:
            print ("0"),
    print "\n"
    p-=1
    l+=1
