'''
https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/little-monk-and-good-string/

Little monk loves good string. Good String is a string that only contains vowels

. Now, his teacher gave him a string S. Little monk is wondering what is the length of the longest good string which is a substring of S.

Note: Strings contains only lower case English Alphabets.

Input:
First line contains a string S,

, where S denotes the length of the string.

Output:
Print an integer denoting the length of the longest good substring, that is substring consists of only vowels.

SAMPLE INPUT
abcaac

SAMPLE OUTPUT
2

Explanation
Longest Good String which is a substring of S is aa so the answer is 2.

'''
a=input()
l=len(a)
globalMax=0
localMax=0
for i in a:
    if( i in 'aeiou'):
        localMax+=1
        globalMax=max(globalMax,localMax)
    else:
        localMax=0
print (globalMax)
