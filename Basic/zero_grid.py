#making the crossponding row/col zero if the given (i,j) is zero
#a=[[1,0,0,0],[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,1]]
#ans = [[0,0,0,0],[0,0,0,0],[0,0,1,1],[0,0,1,1],[0,0,0,0]]

def opr(a,m,n):
    row=[True]*m
    col=[True]*n
    # for row 
    for i in range(m):
        for j in range(n):                
            if a[i][j] == 0:
                row[i] &= False
            
    # for col
    for j in range(n):
        for i in range (m):        
            if a[i][j] == 0:
                col[j] &= False

    # manipulating array
    for i in range(m):
        for j in range(n):
            if row[i] and col[j] :
                a[i][j] = 1
            else:
                a[i][j] = 0
            
            #print (i and j, end=" ")
        #print ()

    return a
                
         
def pnt(a):
    for i in a:
        for j in i :
            print (j,end=" ")
        print ()



a=[[1,0,1,1],[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,1]]
m=len(a)
n=len(a[0])
print ("original")
pnt(a)
print()
a=opr(a,m,n)
print()
print ("manipulated")
pnt(a)


a=[[1,1,1],[1,1,1],[1,0,1],[1,1,1],[1,1,1],[1,1,0]]
print ("original")
pnt(a)
print()
print ("manipulated")
pnt(opr(a,len(a),len(a[0])))
print()

a=[[1,1,1],[1,1,1],[1,0,1]]
print ("original")
pnt(a)
print()
print ("manipulated")
pnt(opr(a,len(a),len(a[0])))
print()

a=[[0,0],[0,0]]
print ("original")
pnt(a)
print()
print ("manipulated")
pnt(opr(a,len(a),len(a[0])))
print()
