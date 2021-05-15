class Solution:
    def LastIndex(self, s, p):
        for i in range(len(s)-1, -1, -1):
            if(s[i] == p):
                print(i)
                return i
        return -1


s = input().strip()
p = input().split()
ob = Solution()
print(ob.LastIndex(s,p))