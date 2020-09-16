def collatz(number):
    if n%2==0:
        print(number//2)
        return number//2
    elif n%2==1:
        res = number*3+1
        print(res)
        return res


try:
    n =  int(input('Enter a number'))
    while n!=1:
        n = collatz(n)
except:
    print('Enter a integer number')
    
