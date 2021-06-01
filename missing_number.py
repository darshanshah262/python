# Python3 program to find
# the mising Number
# getMissingNo takes list as argument
def getMissingNo(a, n):
	n_elements_sum=n*(n+1)//2
	return n_elements_sum-sum(a)


# Driver program to test above function
if __name__=='__main__':

	a = [1, 2, 4, 5, 6]
	n = len(a)+1
	miss = getMissingNo(a, n)
	print(miss)
