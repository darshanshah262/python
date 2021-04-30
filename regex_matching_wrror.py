'''
The first line contains integer T, the number of test cases.
The next T lines contains the string 
sample input 
2
.*\+
.*+
o/p
True
False
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))