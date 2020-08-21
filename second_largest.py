if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


win = max(arr)

while max(arr) == win:
    arr.remove(max(arr))

print(max(arr))


''' 
under logic part this can also be used:

for i in arr:  
    if i == win:
        arr.remove(i)
