class Solution:  
    def findMean(self, arr, queries, n, q): 
        # Complete the function
        self.presumarr=[]
        self.templist=[]
        self.arrsum=0
        
        for k in range(len(arr)):
            self.arrsum += arr[k]
            self.presumarr.append(self.arrsum)

        for i in range(0,q,2):
            self.sum=0
            self.l=queries[i]
            self.r=queries[i+1]
            self.count = self.r - self.l + 1
            self.templist.append(int(sum(arr[self.l:self.r+1])/self.count))
        return(self.templist)
        
n,q = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))
queries = list(map(int,input().strip().split()))
ob=Solution()
v = ob.findMean(arr, queries, n, 2*q)
print(v)