'''
Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4

Explanation
When we perform  left rotations, the array undergoes the following sequence of changes:
[1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]
Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
'''

#!/bin/python

from __future__ import print_function

import os
import sys

if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())
    
    ln = len(a)
    for i in range(d):
        tmp=a[0]
        a.remove(a[0])
        a.append(tmp)
    for i in a:
        print (i,end=" ")
