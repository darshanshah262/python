Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
 
      
a = sorted(l)[1]
names = []
for n,s  in l:
    if s == a[1]:
        names.append(n)

for x in sorted(names):
    print(x)
    
    
    
    
    
    
    
 '''
if __name__ == '__main__':
    d = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d.update({name : score})
 
        

l = []

for i in d.values():
    l.append(i)

l.sort()
m = min(l)
while min(l) == m:
    l.remove(min(l))

min_score = min(l)

na = []
for n,s in d.items():
    if min_score == s:
        na.append(n)
    
na.sort()        
for i in na:
    print(i)
'''
