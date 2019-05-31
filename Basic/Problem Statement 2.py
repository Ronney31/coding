# Problem Statement 2

def problem2(lst):
    lst.sort()
    l = len(lst)
    if l %2==0:
    	# for even
        for i in range(l//2):
            print (lst[i],lst[l-(i+1)],end=" ")
    else:
    	# for odd
        for i in range(l//2):
            print (lst[i],lst[l-(i+1)],end=" ")
        print (lst[i+1])

'''
	if input is like:-
		input :- 1 4 7 9 1 3 5 10 11
		output:- 1 11 1 10 3 9 4 7 5
	time complexity :- Big O (nlogn)
	space complexity:- Big O (1)
'''

input_array = list(map(int, input().strip().split()))

problem2(input_array)
