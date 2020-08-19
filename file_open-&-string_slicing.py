fname = input("Enter file name: ")
fh = open(fname)
num = 0.0
count = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    x = line.find(':')
    y = line[x+1:]
    num = num + float(y)
    avg = num / count
print('Average spam confidence:',avg)
