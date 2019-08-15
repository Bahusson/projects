#Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
#fh = open('mbox-short.txt')

fh = open('mbox-short.txt')
count = 0
total=0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ipos = line.find(':')
    count = count + 1
    line2 = (line[ipos+2:])
    value = float(line2)

total = total + value

#print ('Total:', suma)
total = value/count
print ('Average:', total)
print ('Line count:', count)
print ('done')
