fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

dt = dict()
for line in fh:
    if line.startswith ('From:') : continue
    if not line.startswith('From') : continue
    line = line.rstrip()
    line = line.split()
    line = line [5]
    line = line.split(':')
    line = line [0]
    dt[line] = dt.get(line,0) + 1

largest = -1
bigword = None
#musi być metoda .items, bo inaczej nie zadziała...
for k,v in sorted(dt.items()) :
    print (k,v)
