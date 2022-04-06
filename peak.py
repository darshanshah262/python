# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, find the index of any one of its peak elements.
# Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 

# Example 1:

# Input:
# N = 3
# arr[] = {1,2,3}
# Output: 2
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.

# Example 2:

# Input:
# N = 2
# arr[] = {3,4}
# Output: 1
# Explanation: 4 (at index 1) is the 
# peak element as it is greater than 
# its only neighbour element 3.

# code

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        # O(n) TC
        # peak = 0
        # for i in range(n-1):
        #     if arr[i] < arr[i+1]:
        #         peak = i + 1
        # return peak
        
        # TC O(log N)
        lb = 0
        ub = n-1
        while lb<ub:
            mid = (lb+ub)//2
            if arr[mid] > arr[mid+1]:
                ub = mid
            else:
                lb= mid+1
                
        return lb

      

#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends
