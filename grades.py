score = input("Enter Score: ")
scr = float(score)
try :
    #score ranges from 0.0 to 1.0
    if scr<=1.0 :
        if scr >= 0.9 :
            print('A')
        elif scr >=0.8 :
            print('B')
        elif scr >= 0.7 :
        	print('C')
        elif scr >=0.6 :
            print('D')
        else :
            print('F')
except :
    print('Enter the grades in the range of 0.0 to 1.0')
    quit()
