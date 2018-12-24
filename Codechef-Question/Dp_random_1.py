#https://www.youtube.com/watch?v=5o-kdjv7FD0
#pending 
def num(n):
	if n == 0 or n ==  1 : return 1
	nums[0] = 1; nums[1] = 1
	for i in range (2, n):
		nums[i] = nums[i-1] + nums[i-2]
	return nums[n]

#num(5)