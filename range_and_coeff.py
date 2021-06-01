def findRangeAndCoefficient(arr):
    mini = min(arr)
    maxi = max(arr)
    print('Range is :',maxi-mini)
    print('Cofficient is:',(maxi-mini)/(mini+maxi))

if __name__ == '__main__':
    arr = [5, 10, 15]
    findRangeAndCoefficient(arr)