while True:
    hrs1 = input("Enter Hours:")
    try:
        hrs = (float(hrs1))
    except:
        print ('giv snek da number not blah blah...')
        continue
    if type(hrs) == float :
        break

while True:
    rat1 = input("Enter Rate:")
    try:
        rat = (float(rat1))
    except:
        print ('giv snek da number not blah blah...')
        continue
    if type(hrs) == float :
        break

ot = (float(hrs) - 40)*0.5
if ot < 0 :
    ot = 0

py = (float(hrs) + float(ot)) * float(rat)
print("Pay:",py)
    #short1()
