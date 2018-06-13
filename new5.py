hrs = input("Enter Hours:")
rat = input("Enter Rate:")

ot = (float(hrs) - 40)*0.5
if ot < 0 :
    ot = 0

py = (float(hrs) + float(ot)) * float(rat)
print("Pay:",py)
