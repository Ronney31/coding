# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:51:09 2018

@author: Sardar
"""

def subsets(nums):
    res = []
    backtrack(res, nums, [], 0)
    return res
 
def backtrack(res, nums, stack, pos):
    if pos == len(nums):
        res.append(list(stack))
    else:
        # take nums[pos]
        stack.append(nums[pos])
        backtrack(res, nums, stack, pos+1)
        stack.pop()
        # dont take nums[pos]
        backtrack(res, nums, stack, pos+1)

 
# simplified backtrack
#def backtrack(res, nums, cur, pos):
    # if pos >= len(nums):
        # res.append(cur)
    # else:
        # backtrack(res, nums, cur+[nums[pos]], pos+1)
        # backtrack(res, nums, cur, pos+1)
 
 
# Iteratively
def subsets2(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res
 
test = [1,2,3]
print(test)
print(subsets(test))
