#LTI coding round2
#sell and add coins
'''
to sell coin total coin value >=y and it changes to previos value

to add coin if total coin value >= X then X + i else X + 2i
'''
def solution(input1,input2,input3,input4):
    #x is total coin value
    x = 0
    c=0
    for i in range(input3):
        operation = input4[i][0]
        value = input4[i][1]
        if operation == 0:
            #adding coin
            prev = x
            x += (2*value) if x<input1 else (value)
            # if value < input1:
            #     x += 2*value
            # else:
            #     x += value
        if operation == 1:
            #selling coin
            # x = prev if x>input2 else x
            if x > input2:
                x = prev
            else:pass

    return x


input1 = int(input())   #X
input2 = int(input())   #Y
input3 = int(input())   #no of coins
input4 = [[0,5],[1,0]]  #operations

print(solution(input1,input2,input3,input4))