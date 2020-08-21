#run the list commands givena as input

if __name__ == '__main__':
    N = int(input())

l = []
for _ in range(N):
    a = input().split()
    cmd = a[0]
    rest = a[1:]
    if cmd != 'print':
        cmd = cmd + "(" + "," .join(rest) + ")" #l.append()
        eval("l."+cmd)
    else :
        print(l)
