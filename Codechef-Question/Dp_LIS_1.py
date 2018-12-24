#https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
a=[10,22,9,33,21,50,41,60]
a_c = []

for i in a:
    a_c.append(1)
#a_c = [1,1,1,1,1,1,1,1]
    
for i in range(1,len(a)):
    for j in range(0,i):
        if(a[j]<a[i]):
            a_c[i] = max(a_c[j]+1 , a_c[i])

print ("LIS =  ",max(a_c))
