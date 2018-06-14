"""
Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases. 
Each test case consist of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if pair of parenthesis are balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 100

Example:

Input:
3
{([])}
()
()[]

Output:
balanced
balanced
balanced
"""

t=int(input())
for i in range(t):
    c=((input().rstrip().split()))
    a=[]
    for i in c[0]:
        a.append(i)
    s=['[','{','(']
    e=[']','}',')']
    stack=[]
    b=0
    for i in range(len(a)):
        if(a[i]==s[0] or a[i]==s[1] or a[i]==s[2] ):
            stack.append(a[i])
        else:
            if(len(stack)==0):
                #print("not balanced")
                b=1
                break
            elif(a[i]==e[0] and stack[-1]==s[0]):
                    stack.pop()
            elif(a[i]==e[1] and stack[-1]==s[1]):
                    stack.pop()
            elif(a[i]==e[2] and stack[-1]==s[2]):
                    stack.pop()
            else:
                b=1
                break
    if(len(stack)==0 and b==0):
        print ("balanced")
    if(len(stack)!=0 or b==1):
        print ("not balanced")
