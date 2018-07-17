#python 3.6 code

def fun(res, arr, newarr, pos, k):
    if pos == len(arr):
        s=0
        for i in newarr:
            s+=a[i]
        if(s>=k):
            res.append(list(newarr))
        
    else:
        newarr.append(arr[pos])
        
        #with taking pos(th) element
        fun(res, arr, newarr, pos+1, k)
        newarr.pop()
        
        #without taking pos(th) element
        fun(res, arr, newarr, pos+1, k)
        
if __name__ == "__main__":
    #here key=ID and Value= credit
    a={1:30,2:70,4:60,5:50,7:80,8:10,3:-250}
    K=150
    res = []
    #fetching key and storing in arr
    arr=[i for i in a]
    fun(res,arr,[],0,K)
    #output the nexted key in array/list whose values satisfying K (condition)
    #print (res,"\n")
    
    # to see the id as well as the credit (together)
    print ("Combination of people that can form a team")
    #global team array
    glteam=[]
    for i in res:
        tmp={}
        for j in i:
            #print (a[j],end=" ")
            tmp[j]=a[j]
        #print (tmp)
        if(len(tmp)<=3):
            print (tmp)
            #glteam.append(i if(i not in glteam) for i in tmp)
            for i in tmp:
                if(i not in glteam):
                    glteam.append(i)
    print ("The total number of people given is ",len(a))
    if(len(glteam)>0):
        print ("The maximum number of people that can form a team is ",len(glteam))
        print ("And the member's are :- ",glteam)

