# Python3 program to find day
# of a given date

def dayofweek(d,m,y):
    t = [0,3,2,5,0,3,5,1,4,6,2,4]
    y -= m < 3
    return ((y + int(y/4) - int(y/100) + int(y/400) + t[m-1] + d) % 7)

#YYYY-MM-DD
'''
3
1998-08-15
2001-02-26
2000-05-04
0-SUNDAY
1-MONDAY

6-SATUARDAY
'''

n =int(input())
days=['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
for i in range(n):
    y,m,d = input().split('-')
    y = int(y)
    m = int(m)
    d = int(d)
    day = dayofweek(d,m,y)
    print(days[day])