'''
Longest Common Subsequence 
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS of "ABC" and "AC" is "AC" of length 2
'''

def f(a,b,i,j,la,lb):
    if(i==la or j==lb):
        return 0;
    if(dp[i][j] == -1):
        if( a[i]==b[j]):
            dp[i][j]=f(a,b,i+1,j+1,la,lb)+1
        else:
            x=f(a,b,i+1,j,la,lb)
            y=f(a,b,i,j+1,la,lb)
            dp[i][j]=max(x,y)

    return dp[i][j]

#main
t=int(input())
for p in range(t):
    la,lb=map(int,input().strip().split())
    a=list(input())
    b=list(input())
    #dp=[[-1]*(max(len(a),len(b)))]*(max(len(a),len(b)))
    dp=[]
    for i in range(len(a)):
        tmp=[]
        for j in range(len(b)):
            tmp.append(-1)
        dp.append(tmp)
    res=f(a,b,0,0,len(a),len(b))
    print (res)
