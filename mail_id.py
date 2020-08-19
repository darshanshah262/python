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
