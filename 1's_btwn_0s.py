a = [1,1,1,1,1,0,0]
i = [index for index, value in enumerate(a) if value == 0]
s=0
for m in range(len(i)-1):
    s += (i[m+1]-i[m]-1)
print(s)