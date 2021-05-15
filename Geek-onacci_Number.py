'''

Input:
3
1 3 2 4
1 3 2 5
1 3 2 6

Output:
6
11
19

'''
def Geek(a,b,c,n):
    sum1=0
    print(a,b,c,n)
    if n==3:
        return c
    else:
        sum1=a+b+c
    return(Geek(b,c,sum1,n-1))

x=int(input())
for i in range(x):
    arr=[int(x) for x in input().strip().split()]
    a,b,c,n=arr[0],arr[1],arr[2],arr[3]
    print(Geek(a,b,c,n))