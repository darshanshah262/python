def sum(a,b):
    #code here
    while(b!=0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

a = int(input())
b = int(input())
print(sum(a,b))


'''
Recurssion

def Add(x, y):
   
    if (y == 0):
        return x
    else
        return Add( x ^ y, (x & y) << 1)
'''