# cook your code here
//code for selection sort

def selection(a):
    l=len(a)
    b=[]
    m=a[0]
    for j in range(0,l):
            
        for i in range(0,(l-1)):
            if(a[i]>a[i+1]):
                a[i],a[i+1] = a[i+1],a[i]
            #print (a)
    for i in a:
        print (i),
#l=int(input())
#nd = raw_input().split()
a = map(int, raw_input().rstrip().split())
selection(a)

