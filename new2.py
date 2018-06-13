
n1 = input ("Countdown from:   ")

try:
    n = int(n1)
except:
    print ('giv snek da number not blah blah...')
    quit()
if n > 50000 :
    print ('your pushin da snek...')
    quit()
elif n <= 0 :
    print ('Ur insane!')
    quit()
while n > 0 :
    print(n)
    n=n-1
print ('Kaboom!')
