class Solution:
    def ReverseSort(self, str): 
        # code here
        str = ''.join(sorted(str,reverse=True))
        return str

s = input().strip()
ob = Solution()
print(ob.ReverseSort(s))