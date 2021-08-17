'''
1st line n no of inputs
next n lines a,b for matrix from 1 till end(a*b)

1
2,1

ans:
[[1],[2]]
'''
def solution(a,b):
    l=[]
    x=1
    for i in range(a):
        lst=[]
        for j in range(b):
            lst.append(x)
            x+=1#x=x+1
        l.append(lst)
    print(l)




n = int(input())
for i in range(n):
    a,b = input().split(',')
    a=int(a)
    b=int(b)
    solution(a,b)