#retriving all the mail_id of senders from a list of mails recieved! in a file


fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
y = list()
for lines in fh :
    lst = lines.split()
    if 'From'in lst :
        print(lst[1])
        count = count +1

print("There were", count, "lines in the file with From as the first word")


#code for most no.of a id has repeated
'''
name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
wrd = dict()
for lines in handle:
    word = lines.split()
    if 'From:' in word :
        w = word[1]
        wrd[w] = wrd.get(w,0) + 1
largest = -1
wd = None
for k,v in wrd.items() :
    if v > largest :
        largest = v
        wd = k
print(wd,largest)
'''
