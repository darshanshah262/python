'''
There are N students in a class. Each student got arr[i] (1 <= i <= N) marks in mathematics exam. Geek loves mathematics and he got X marks. Now geek is curious to know, how many students in his class got marks greater than that of Geek's.

Input:
1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
2. The first line of each test case contains two space-separated integers N and X.
3. The second line contains N space-separated positive integers represents array arr.

Output: For each test case, print the count of students who got marks greater than X.

Constraints:
1 <= T <= 10
1 <= N <= 100000
1 <= arr[i], K <= 100000

Example:
Sample Input:
2
3 2
4 1 3
4 9
4 8 1 2

Sample Output:
2
0

Explanation:
Testcase 1: Students with marks 4 and 3 got higher marks than Geek who got 2 marks. 


'''



t = int(input())
while t:
    s=0
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    '''
    for i in arr:
        if i > x:
            s += 1
    print(s)
    '''
    print(sum([1 for i in arr if i>x]))
    t-=1