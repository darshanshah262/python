'''
n,k - 5 2
n inputs
1
2
3
4
5

print count and numbers

'''

def relation(n,k):
    l=[]
    a =[]
    c=0
    for i in range(n):
        l.append(int(input()))
    for i in range(len(l)):
        if (n-l[i]) % k == 0:
            c+=1
            a.append(l[i])
    print(c)
    for i in a:
        print(i)

n,k = map(int,input().split())
relation(n,k)