'''
M = 4, N = 3
Arr1 = {1 , 0, 3, 2}
Arr2 = {2, 0, 4}
Output: {2, 0, 10, 4, 12, 8}
Explaination: 
First polynomial: 
1 + 0x1 + 3x2 + 2x3
Second polynomial: 
2 + 0x1 + 4x2
Product polynomial:
2 + 0x1 + 10x2 + 4x3 + 12x4 + 8x5
'''

class Solution:
	def polyMultiply(self, Arr1, Arr2, M, N):
		# code here
		l = [0]*(M+N-1)
		for i in range(len(Arr1)):
		    for j in range(len(Arr2)):
		        l[i+j] += Arr1[i] * Arr2[j]
		return l

M,N = map(int,input().split())
M = int(M)
N = int(N)
Arr1 = input().split()
for i in range(M):
    Arr1[i] = int(Arr1[i])

Arr2 = input().split()
for i in range(N):
    Arr2[i] = int(Arr2[i])

ob = Solution()
ans = ob.polyMultiply(Arr1,Arr2,M,N)
for i in range(len(ans)):
    print(ans[i],end=" ")