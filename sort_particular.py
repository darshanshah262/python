# def sort_array(source_array):
#     b = sorted([n for n in source_array if  n % 2 != 0])
#     c = -1
#     d = []
#     for i in source_array:
#         c = c+1
#         if i % 2 != 0 :
#             d.append(c)
#     print(d)
#     for x in range (len(d)):
#         z = d[x]
#         source_array[z] = b[x]
#     return source_array

# a = [1,3,4,5,6,4,6,3,2,1,7]
# print(sort_array(a))

def solution(l):
    even = []
    d={}
    for i in range(len(l)):
        d[i] = l[i]
        if l[i] % 2 == 0:
            even.append(l[i])
    even.sort()
    ind = 0
    for k,v in d.items():
        if v % 2 == 0:
            d[k] = even[ind]
            ind +=1
    return(list(d.values()))

l = [1,3,4,5,6,4,6,3,2,1,7]
print(solution(l))