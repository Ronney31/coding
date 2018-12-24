for _ in range(int(input())):
    a,b=map(int,input().strip().split())
    if(a==b):
        print ("YES")
    elif(a<b):
        while(a!=b):
            a+=1
        if(a==b):
            print ("YES")
    elif(a>b):
        while(a!=b):
            b+=1
        if(a==b):
            print ("YES")
    else:
        print ("NO")
