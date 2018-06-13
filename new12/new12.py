import re
fname = input("Enter file:")
if len(fname) < 1 : fname = "sample.txt"
fh = open(fname)

numlist = list()
for line in fh:
    num = re.findall ('([0-9]+)', line)
    numlist = numlist + num
    #print(numlist)

sum = 0
for value in numlist:
    sum = sum + int(value)

print (sum)
