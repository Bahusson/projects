text = 'X-DSPAM-Confidence:    0.8475'
position = text.find(':')
#print(position)
number = text[position+5:]
#print(number)
value = float(number)
print(value)
