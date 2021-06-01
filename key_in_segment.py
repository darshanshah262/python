'''
Input : 
arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3} 
x = 3 
k = 3 
Output : Yes 
There are 4 non-overlapping segments of size k in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
Input : 
arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25} 
x = 23 
k = 5 
Output :Yes 
There are three segments and last segment is not full {21, 23, 56, 65, 34}, {54, 76, 32, 23, 45} and {21, 23, 25}. 
23 is present all window.
'''

# Python 3 program to find
# the every segment size of
# array have a search key x

def findxinkindowSize(arr, x, k, n) :

	i = 0
	while i < n :

		j = 0
		# Search x in segment
		# starting from index i
		while j < k :
			if arr[i + j] == x :
				break
			j += 1
		# If loop didn't break
		if j == k :
			return False
		i += k
	# If n is a multiple of k
	if i == n :
		return True
	j = i - k
	# Check in last segment if n
	# is not multiple of k.
	while j < n :
		if arr[j] == x :
			break
		j += 1
	if j == n :
		return False
	return True

# Driver Code
if __name__ == "__main__" :

	arr = [ 3, 5, 2, 4, 9, 3,
			1, 7, 3, 11, 12, 11]
	x, k = 3, 3
	n = len(arr)
	if (findxinkindowSize(arr, x, k, n)) :
		print("Yes")
	else :
		print("No")