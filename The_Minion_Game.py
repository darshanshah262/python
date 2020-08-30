def minion_game(s):
    v = 'AEIOU'
    ks = 0
    ss = 0

    for i in s:
        s = s.replace(i,i.upper())

    for i in range(len(s)):
        if s[i] in v:
            ks += (len(s) - i)
        else :
            ss += (len(s) - i)
    if ks > ss:
        print('Kevin', ks)
    elif ss > ks:
        print('Stuart', ss)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
