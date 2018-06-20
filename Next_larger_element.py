'''
Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A[ ].
 
Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1<=T<=200
1<=N<=1000
1<=A[i]<=1000

Example:
Input
1
4
1 3 2 4 

Output
3 4 4 -1

Explanation
In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
'''
t=int(input())
for i in range(t):
    n=int(input()) 
    a=list(map(int,input().rstrip().split()))
    stack=[]
    result=[]
    for i in range(n-1, -1,-1):
        if(i==n-1):
            result.append(-1)
            stack.append(a[i])
        else:
            if(a[i]<stack[-1]):
                result.append(stack[-1])
                stack.append(a[i])
            else:
                if(max(stack)>a[i]):
                    z=0
                    while(a[i]<stack[z]):
                        z+=1
                    stack=stack[0:z]
                    result.append(stack[-1])
                else:
                    stack.clear()
                    #stack.append(a[i])
                    result.append(-1)
                stack.append(a[i])
    result.reverse()
    for i in result:
        print(i,end=" ")
    print ()
