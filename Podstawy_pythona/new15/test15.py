import re

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox.txt'
fh = open(fname)
sum = 0
lst = list()
for line in fh:
#    org1 = re.findall ('@(.*?)>', line)
    sak = re.findall ('@(sakaiproject*?)>', line)
    lst.append(sak)

for item in lst:
    sum = sum +1
#    if len(org) > 0:
print(sum)
