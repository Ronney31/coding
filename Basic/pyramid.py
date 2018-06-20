'''
https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/little-monk-and-his-toy-story/

Little Monk has N number of toys, where each toy has some width Wi. Little Monk wants to arrange them in a pyramdical way with two simple conditions in his mind. The first being that the total width of the ith row should be less than (i+1)th row. The second being that the total number of toys in the ith row should be less than (i+1)th row. Help Monk find the maximum height which is possible to be attained!

Note: It is NOT necessary to use all the boxes.

Input format:
The first line contains an integer N, which denotes the number of Monk's toys. The next line contains N integers each denoting the width of the Monk's every single toy.

Output format:
Print the maximum height of the toy pyramid.

SAMPLE INPUT
4
40 100 20 30

SAMPLE OUTPUT
2

Explanation

On the lowest level, we can place 20 and 100, and on top of it we can place 40 , so the maximum height would be 2.

'''
t=int(input())
b=list(map(int,input().rstrip().split()))
b.sort() #20,30,40,100
b.reverse() #100,40,30,20
l=[]
j=0
r=[]
for i in range(len(b)):
    #l.append(b[-1:j])
    tmp=[]
    for j in range(0,i+1):
        if(len(b)==0):
            
            break
        tmp.append(b.pop())
    if(len(tmp) != 0) :
        l.append(tmp)
        if(len(l[i])>len(l[i-1]) and (sum(l[i])>sum(l[i-1]))):
            r.append(l.copy())
    #j+=1
if(len(r) == 0):
    print (1)
else:
    print (len(r[-1]))
