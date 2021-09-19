def solution(input1):

    arr = [0]*26
    n = len(input1)
    l= -10 ** 8

    for i in range(n):
        x = ord(input1[i]) - ord('a')
        a = 0

        for j in range(x):
            a = max(a, arr[j])

        a += 1
        l = max(l, a)
        arr[x] = max(arr[x],a)

    return l


print(solution('bcdabdz'))
