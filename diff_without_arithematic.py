def diff(x,y):
    while(y!=0):
        borrow = ~x & y
        x = x ^ y
        y =borrow << 1
    return x

a  = int(input())
b = int(input())
print(diff(a,b))


'''
recurssion

def diff(x,y):
    if (y == 0):
        return x
    return subtract(x ^ y, (~x & y) << 1)
'''