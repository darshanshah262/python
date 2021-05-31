class Solution:
    def repeatedSubtraction(self, A, B):
        #code here
        if A==B:
            return 1
        if A>B:
            if A%B == 0:
                return A//B
            else:
                return (A//B) + self.repeatedSubtraction(B,(A%B))
        else:
            if B%A == 0:
                return B//A
            else:
                return (B//A) + self.repeatedSubtraction(A,(B%A))

a = int(input())
b = int(input())
ob = Solution()
print(ob.repeatedSubtraction(a,b))


'''
Given two integers A and B.Find out the number of steps required to repeatedly subtract 
the smaller of the two from the larger until one of them becomes 0.

Input:
A=5,B=13
Output:
6
Explanation:
The steps are as follows:
(5,13)->(5,8)->(5,3)->(2,3)->(2,1)->(1,1)->(1,0)
Thus, 6 steps are required.
'''